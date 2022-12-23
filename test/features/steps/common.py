from behave import given, when, then
import requests


@given(u'path to server is "{server_url}"')
def server_path(context, server_url):
    context.server_url = server_url


@when(u'I call endpoint "{endpoint}"')
def call_endpoint(context, endpoint):
    assert context.server_url
    context.res = requests.get(context.server_url + endpoint)


@then(u'I should get an OK')
def assert_ok(context):
    assert context.res.status_code == 200
