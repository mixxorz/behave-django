from behave import given, when, then
from django.core.urlresolvers import reverse


@given(u'get_url(reverse="{reverse_arg}") returns a different value than '
       u'get_url(path="{path_arg}")')
def ensure_different(context, reverse_arg, path_arg):
    assert \
        context.get_url(reverse=reverse_arg) != context.get_url(path=path_arg)


@when(u'I call get_url() without arguments')
def without_args(context):
    context.__result = context.get_url()


@when(u'I call get_url("{path_arg}") with one positional argument')
def one_positional_arg(context, path_arg):
    context.__result = context.get_url(path_arg)


@when(u'I call get_url("{path_arg}", "{reverse_arg}") '
      u'with two positional arguments')
def two_positional_args(context, path_arg, reverse_arg):
    context.__result = context.get_url(path_arg, reverse_arg)


@when(u'I call get_url(reverse="{reverse_arg}") '
      u'with the reverse keyword argument')
def one_keyword_arg(context, reverse_arg):
    context.__result = context.get_url(reverse=reverse_arg)


@when(u'I call get_url(reverse="{reverse_arg}", path="{path_arg}") '
      u'with two keyword arguments')
def two_keyword_args(context, reverse_arg, path_arg):
    context.__result = context.get_url(reverse=reverse_arg, path=path_arg)


@then(u'it returns the value of base_url')
def is_baseurl_value(context):
    assert context.base_url == context.__result


@then(u'the result is the base_url with "{path_arg}" appended')
def baseurl_plus_path(context, path_arg):
    assert context.base_url + path_arg == context.__result


@then(u'this returns the same result as get_url(reverse("{reverse_arg}"))')
def explicit_reverse(context, reverse_arg):
    assert context.get_url(reverse(reverse_arg)) == context.__result


@then(u'this returns the same result as get_url("{path_arg}")')
def implicit_path_arg(context, path_arg):
    assert context.get_url(path_arg) == context.__result
