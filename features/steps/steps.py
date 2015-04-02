import urllib2

from behave import given, when, then


@given(u'this step exists')
def step_exists(context):
    pass


@when(u'I run "python manage.py behave"')
def run_command(context):
    pass


@then(u'I should see the behave tests run')
def is_running(context):
    pass


@when(u'I visit "{url}"')
def visit(context, url):
    context.response = urllib2.urlopen(context.base_url + url).read()
    

@then(u'I should see "{text}"')
def i_should_see(context, text):
    assert text in context.response
