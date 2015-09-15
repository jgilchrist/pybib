from pybib import utils
from hamcrest import *

from nose.tools import assert_raises

import requests
import requests_mock

class MockRequest:
    def __init__(self, code):
        self.code = code

    @property
    def status_code(self):
        return self.code

def test_handle_status_code_200():
    utils.handle_status_code(MockRequest(200))

def test_handle_status_code_404():
    with assert_raises(SystemExit):
        utils.handle_status_code(MockRequest(404))

def test_handle_status_code_unknown():
    with assert_raises(SystemExit):
        utils.handle_status_code(MockRequest(1))

def test_search():
    search_json_response = """
    {
        "message-version": "1.0.0",
        "message": {
            "facets": {},
            "query": {
                "start-index": 0,
                "search-terms": "test"
            },
            "total-results": 1,
            "items": [{
                "source": "CrossRef",
                "title": ["Test Citation"],
                "type": "dissertation", "URL": "http://dx.doi.org/test.doi",
                "deposited": {"timestamp": 1000, "date-parts": [[2015, 1, 1]]},
                "container-title": [],
                "author": [{"given": "Test", "affiliation": [], "family": "Test"}],
                "reference-count": 0,
                "member": "http://id.crossref.org/member/xxx",
                "subtitle": [],
                "indexed": { "timestamp": 1000, "date-parts": [[2015, 1, 1]] },
                "prefix": "http://id.crossref.org/prefix/test",
                "publisher": "Test Publisher",
                "score": 1.0,
                "DOI": "test.doi",
                "issued": { "date-parts": [[]] }
            }]
        }
    }
    """

    with requests_mock.mock() as m:
        m.get('http://api.crossref.org/works', text=search_json_response)
        entries = utils.search('test.doi')


        print(entries)

    assert_that(len(entries), equal_to(1))

    entry = entries[0]
    assert_that(entry["title"], equal_to(["Test Citation"]))

def test_get_bibtex():
    with requests_mock.mock() as m:
        m.get('http://dx.doi.org/test.doi', text='abc')
        entry = utils.get_bibtex('test.doi')

    assert_that(entry, equal_to('abc'))
