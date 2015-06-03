from behave import when, then
from django.core.urlresolvers import reverse

from test_app.models import BehaveTestModel


@when(u'I call get_url() without arguments')
def without_args(context):
    context.__result = context.get_url()


@when(u'I call get_url("{url_path}") with an absolute path')
def path_arg(context, url_path):
    context.__result = context.get_url(url_path)


@when(u'I call get_url("{view_name}") with a view name')
def view_arg(context, view_name):
    context.__result = context.get_url(view_name)


@when(u'I call get_url(model) with a model instance')
def model_arg(context):
    context.__model = BehaveTestModel(name='Foo', number=3)
    context.__result = context.get_url(context.__model)


@then(u'it returns the value of base_url')
def is_baseurl_value(context):
    assert context.base_url == context.__result


@then(u'the result is the base_url with "{url_path}" appended')
def baseurl_plus_path(context, url_path):
    assert context.base_url + url_path == context.__result


@then(u'this returns the same result as get_url(reverse("{view_name}"))')
def explicit_reverse(context, view_name):
    reversed_view = reverse(view_name)
    assert context.get_url(reversed_view) == context.__result


@then(u'this returns the same result as get_url(model.get_absolute_url())')
def get_model_url(context):
    path = context.__model.get_absolute_url()
    assert context.get_url(path) == context.__result
