from pybib import formatters as mod
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
    formatted_entry = mod.format_entry(mock_entry)

    assert_that(formatted_entry, contains_string('Test'))
    assert_that(formatted_entry, contains_string('T. Author'))
    assert_that(formatted_entry, contains_string('2015'))
    assert_that(formatted_entry, contains_string('Journal Article'))

def test_color_parts():
    parts = mod.get_common_parts(mock_entry)
    parts = mod.color_parts(parts)

    assert_that(parts.title, contains_string('\x1b['))
    assert_that(parts.doi, contains_string('\x1b['))

def test_get_common_parts():
    parts = mod.get_common_parts(mock_entry)

    assert_that(parts.type, equal_to('Unknown'))
    assert_that(parts.title, equal_to('Test'))
    assert_that(parts.authors, equal_to('T. Author'))
    assert_that(parts.date, equal_to(2015))
    assert_that(parts.container, equal_to('Test Container'))
    assert_that(parts.doi, equal_to('test.doi.010101'))


# The following tests are currently placeholders

def test_format_book():
    parts = mod.get_common_parts(mock_entry)
    assert_that(mod.format_book(mock_entry, parts), equal_to(''))

def test_format_book_chapter():
    parts = mod.get_common_parts(mock_entry)
    assert_that(mod.format_book_chapter(mock_entry, parts), equal_to(''))

def test_format_component():
    parts = mod.get_common_parts(mock_entry)
    assert_that(mod.format_component(mock_entry, parts), equal_to(''))

def test_format_dataset():
    parts = mod.get_common_parts(mock_entry)
    assert_that(mod.format_dataset(mock_entry, parts), equal_to(''))

def test_format_dissertation():
    parts = mod.get_common_parts(mock_entry)
    assert_that(mod.format_dissertation(mock_entry, parts), equal_to(''))

def test_format_journal():
    parts = mod.get_common_parts(mock_entry)
    assert_that(mod.format_journal(mock_entry, parts), equal_to(''))

def test_format_journal_article():
    parts = mod.get_common_parts(mock_entry)
    assert_that(mod.format_journal_article(mock_entry, parts), equal_to(''))

def test_format_monograph():
    parts = mod.get_common_parts(mock_entry)
    assert_that(mod.format_monograph(mock_entry, parts), equal_to(''))

def test_format_proceedings_article():
    parts = mod.get_common_parts(mock_entry)
    assert_that(mod.format_proceedings_article(mock_entry, parts), equal_to(''))

def test_format_reference_entry():
    parts = mod.get_common_parts(mock_entry)
    assert_that(mod.format_reference_entry(mock_entry, parts), equal_to(''))

def test_format_report():
    parts = mod.get_common_parts(mock_entry)
    assert_that(mod.format_report(mock_entry, parts), equal_to(''))

def test_format_standard():
    parts = mod.get_common_parts(mock_entry)
    assert_that(mod.format_standard(mock_entry, parts), equal_to(''))

def test_format_unknown():
    parts = mod.get_common_parts(mock_entry)
    assert_that(mod.format_unknown(mock_entry, parts), equal_to(''))
