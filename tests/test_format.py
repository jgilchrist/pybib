from pybib import formatters
from hamcrest import *

mock_entry = {
    'deposited': { 'date-parts': [[2015, 1, 1]], 'timestamp': 1000 },
    'subject': ['General'],
    'DOI': 'test.doi.010101',
    'reference-count': 0,
    'URL': 'http://dx.doi.org/test.doi.010101',
    'title': ['Test'],
    'score': 0.0,
    'issued': {'date-parts': [[2015, 1, 1]]},
    'subtitle': [],
    'author': [{'family': 'Author', 'given': 'The', 'affiliation': []}],
    'page': '1-10',
    'issue': '1',
    'volume': '1',
    'source': 'CrossRef',
    'publisher': 'Test Publisher',
    'container-title': ['Test Container'],
    'ISSN': ['XXXX'],
    'indexed': {'date-parts': [[2015, 1, 1]], 'timestamp': 1000 },
    'member': 'http://id.crossref.org/member/1',
    'type': 'journal-article',
    'prefix': 'http://id.crossref.org/prefix/test'
}

def assert_handles_absence(field, expected):
    mock_entry_without_field = mock_entry.copy()
    mock_entry_without_field[field] = []
    formatted_entry = formatters.format_entry(mock_entry_without_field)

    assert_that(formatted_entry, contains_string(expected))

def expect_format(method, expected):
    parts = formatters.get_common_parts(mock_entry)
    assert_that(method(mock_entry, parts), equal_to(expected))

def expect_empty_format(method):
    expect_format(method, '')



def test_format_entry():
    formatted_entry = formatters.format_entry(mock_entry)

    assert_that(formatted_entry, contains_string('Test'))
    assert_that(formatted_entry, contains_string('T. Author'))
    assert_that(formatted_entry, contains_string('2015'))
    assert_that(formatted_entry, contains_string('Journal Article'))

def test_color_parts():
    parts = formatters.get_common_parts(mock_entry)
    parts = formatters.color_parts(parts)

    assert_that(parts.title, contains_string('\x1b['))
    assert_that(parts.doi, contains_string('\x1b['))

def test_get_common_parts():
    parts = formatters.get_common_parts(mock_entry)

    assert_that(parts.type, equal_to('Unknown'))
    assert_that(parts.title, equal_to('Test'))
    assert_that(parts.authors, equal_to('T. Author'))
    assert_that(parts.date, equal_to(2015))
    assert_that(parts.container, equal_to('Test Container'))
    assert_that(parts.doi, equal_to('test.doi.010101'))

def test_handles_title_absence():
    assert_handles_absence('title', expected='No Title')

def test_handles_author_absence():
    assert_handles_absence('author', expected='Anonymous')


# The following tests are currently placeholders

def test_empty_formats():

    empty_formatters = [
        formatters.format_book,
        formatters.format_book_chapter,
        formatters.format_component,
        formatters.format_dataset,
        formatters.format_dissertation,
        formatters.format_journal,
        formatters.format_journal_article,
        formatters.format_monograph,
        formatters.format_proceedings_article,
        formatters.format_reference_entry,
        formatters.format_report,
        formatters.format_standard,
        formatters.format_unknown,
    ]

    for func in empty_formatters:
        expect_empty_format(func)
