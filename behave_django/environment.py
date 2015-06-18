from django.core.management import call_command
try:
    from django.shortcuts import resolve_url
except ImportError:
    # support Django 1.4, which has no resolve_url() yet
    from django.shortcuts import redirect
    resolve_url = lambda to, *args, **kwargs: \
        redirect(to, *args, **kwargs)['Location']

from behave_django.testcase import BehaveDjangoTestCase


def before_scenario(context, scenario):
    # This is probably a hacky method of setting up the test case
    # outside of a test runner. Suggestions are welcome. :)

    context.test = BehaveDjangoTestCase()
    context.test.setUpClass()
    context.test()

    # Load fixtures
    if getattr(context, 'fixtures', None):
        call_command('loaddata', *context.fixtures, verbosity=0)

    context.base_url = context.test.live_server_url

    def get_url(to=None, *args, **kwargs):
        return context.base_url + (
            resolve_url(to, *args, **kwargs) if to else '')

    context.get_url = get_url


def after_scenario(context, scenario):
    context.test.tearDownClass()
    del context.test
