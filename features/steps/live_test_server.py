import urllib2

from behave import when, then


@when(u'I visit "{url}"')
def visit(context, url):
    context.response = urllib2.urlopen(context.base_url + url).read()


@then(u'I should see "{text}"')
def i_should_see(context, text):
    assert text in context.response
