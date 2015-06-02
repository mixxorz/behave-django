from behave import given, when, then
from django.core.urlresolvers import reverse


@given(u'get_url(reverse="{reverse_arg}") returns a different value than get_url(path="{path_arg}")')
def step_impl(context, reverse_arg, path_arg):
    assert context.get_url(reverse=reverse_arg) != context.get_url(path=path_arg)


@when(u'I call get_url() without arguments')
def step_impl(context):
    context.__result = context.get_url()


@when(u'I call get_url("{path_arg}") with one positional argument')
def step_impl(context, path_arg):
    context.__result = context.get_url(path_arg)


@when(u'I call get_url("{path_arg}", "{reverse_arg}") with two positional arguments')
def step_impl(context, path_arg, reverse_arg):
    context.__result = context.get_url(path_arg, reverse_arg)


@when(u'I call get_url(reverse="{reverse_arg}") with the reverse keyword argument')
def step_impl(context, reverse_arg):
    context.__result = context.get_url(reverse=reverse_arg)


@when(u'I call get_url(reverse="{reverse_arg}", path="{path_arg}") with two keyword arguments')
def step_impl(context, reverse_arg, path_arg):
    context.__result = context.get_url(reverse=reverse_arg, path=path_arg)


@then(u'it returns the value of base_url')
def step_impl(context):
    assert context.base_url == context.__result


@then(u'the result is the base_url with "{path_arg}" appended')
def step_impl(context, path_arg):
    assert context.base_url + path_arg == context.__result


@then(u'this returns the same result as get_url(reverse("{reverse_arg}"))')
def step_impl(context, reverse_arg):
    assert context.get_url(reverse(reverse_arg)) == context.__result


@then(u'this returns the same result as get_url("{path_arg}")')
def step_impl(context, path_arg):
    assert context.get_url(path_arg) == context.__result
