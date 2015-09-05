from pybib import utils
from hamcrest import *

from nose.tools import assert_raises

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
