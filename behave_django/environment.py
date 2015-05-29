from django.core.management import call_command
from django.core.urlresolvers import reverse as url_reverse

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

    def get_url(path=None, reverse=None):
        """
        URL helper attached to context with built-in reverse resolution as a
        handy shortcut. Takes either a path or a reverse name.  Examples::

            context.get_url()
            context.get_url('/path/to/page/')
            context.get_url(reverse='resource-name')
            context.get_url(reverse('resource-name'))
            context.get_url(reverse('resource-name', 'args', and='kwargs'))
        """
        if path is not None:
            return context.base_url + path
        elif reverse is not None:
            return context.base_url + url_reverse(reverse)
        else:
            return context.base_url

    context.get_url = get_url


def after_scenario(context, scenario):
    context.test.tearDownClass()
    del context.test
