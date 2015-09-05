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

    mock_entry_without_title = mock_entry.copy()
    mock_entry_without_title['title'] = []
    formatted_entry = formatters.format_entry(mock_entry_without_title)

    assert_that(formatted_entry, contains_string('No Title'))

def test_handles_author_absence():

    mock_entry_without_author = mock_entry.copy()
    mock_entry_without_author['author'] = []
    formatted_entry = formatters.format_entry(mock_entry_without_author)

    assert_that(formatted_entry, contains_string('Anonymous'))


# The following tests are currently placeholders

def test_format_book():
    parts = formatters.get_common_parts(mock_entry)
    assert_that(formatters.format_book(mock_entry, parts), equal_to(''))

def test_format_book_chapter():
    parts = formatters.get_common_parts(mock_entry)
    assert_that(formatters.format_book_chapter(mock_entry, parts), equal_to(''))

def test_format_component():
    parts = formatters.get_common_parts(mock_entry)
    assert_that(formatters.format_component(mock_entry, parts), equal_to(''))

def test_format_dataset():
    parts = formatters.get_common_parts(mock_entry)
    assert_that(formatters.format_dataset(mock_entry, parts), equal_to(''))

def test_format_dissertation():
    parts = formatters.get_common_parts(mock_entry)
    assert_that(formatters.format_dissertation(mock_entry, parts), equal_to(''))

def test_format_journal():
    parts = formatters.get_common_parts(mock_entry)
    assert_that(formatters.format_journal(mock_entry, parts), equal_to(''))

def test_format_journal_article():
    parts = formatters.get_common_parts(mock_entry)
    assert_that(formatters.format_journal_article(mock_entry, parts), equal_to(''))

def test_format_monograph():
    parts = formatters.get_common_parts(mock_entry)
    assert_that(formatters.format_monograph(mock_entry, parts), equal_to(''))

def test_format_proceedings_article():
    parts = formatters.get_common_parts(mock_entry)
    assert_that(formatters.format_proceedings_article(mock_entry, parts), equal_to(''))

def test_format_reference_entry():
    parts = formatters.get_common_parts(mock_entry)
    assert_that(formatters.format_reference_entry(mock_entry, parts), equal_to(''))

def test_format_report():
    parts = formatters.get_common_parts(mock_entry)
    assert_that(formatters.format_report(mock_entry, parts), equal_to(''))

def test_format_standard():
    parts = formatters.get_common_parts(mock_entry)
    assert_that(formatters.format_standard(mock_entry, parts), equal_to(''))

def test_format_unknown():
    parts = formatters.get_common_parts(mock_entry)
    assert_that(formatters.format_unknown(mock_entry, parts), equal_to(''))
