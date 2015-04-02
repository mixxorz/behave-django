import urllib2

from behave import given, when, then

from test_app.models import BehaveTestModel


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
    

@when(u'I save the object')
def save_object(context):
    BehaveTestModel.objects.create(name='Behave Works', number=123)


@then(u'I should only have one object')
def should_have_only_one_object(context):
    assert 1 == BehaveTestModel.objects.count()

    
@when(u'I use the unittest assert library')
def use_assert_library(context):
    # If one of them works, all of them work. ;)
    context.test.assertEqual(1, 1)
    
@when(u'I use the django assert library')
def use_assert_library(context):
    response = context.test.client.get('/')
    context.test.assertTemplateUsed(response, 'index.html')
    

@then(u'it should work properly')
def asserts_should_work(context):
    pass


@when(u'I use django\'s test client to visit "{url}"')
def use_django_client(context, url):
    context.response = context.test.client.get(url)


@then(u'it should return a successful response')
def it_should_be_successful(context):
    assert context.response.status_code == 200
