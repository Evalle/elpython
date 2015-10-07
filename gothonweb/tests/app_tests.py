from nose.tools import *
from bin.app import app
from tests.tools import assert_reponse

def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_repsonse(resp, status="404")

    #test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)
