import warnings

from behave.runner import ModelRunner
from django.core.management import call_command

try:
    from django.shortcuts import resolve_url
except ImportError:
    # support Django 1.4, which has no resolve_url() yet
    from django.shortcuts import redirect
    resolve_url = lambda to, *args, **kwargs: \
        redirect(to, *args, **kwargs)['Location']


class BehaveHooksMixin(object):

    """Provides methods that run during test execution

    These methods are attached to behave via monkey patching.
    """
    testcase_class = None

    def before_scenario(self, context):
        """Method that runs before behave's before_scenario function

        Sets up the test case, base_url, and the get_url() utility function.
        """
        context.test = self.testcase_class()
        context.test.setUpClass()
        context.test()

        context.base_url = context.test.live_server_url

        def get_url(to=None, *args, **kwargs):
            return context.base_url + (
                resolve_url(to, *args, **kwargs) if to else '')

        context.get_url = get_url

    def load_fixtures(self, context):
        """Method that runs immediately after behave's before_scenario function

        If fixtures are found in context, loads the fixtures using the loaddata
        management command.
        """
        if getattr(context, 'fixtures', None):
            call_command('loaddata', *context.fixtures, verbosity=0)

    def after_scenario(self, context):
        """Method that runs immediately after behave's after_scenario function
        """
        context.test.tearDownClass()
        del context.test


def monkey_patch_behave(django_test_runner):
    """Integrate behave_django in behave via before/after scenario hooks."""
    behave_run_hook = ModelRunner.run_hook

    def run_hook(self, name, context, *args):
        if name == 'before_scenario':
            django_test_runner.before_scenario(context)
        behave_run_hook(self, name, context, *args)
        if name == 'before_scenario':
            django_test_runner.load_fixtures(context)
        if name == 'after_scenario':
            django_test_runner.after_scenario(context)

    ModelRunner.run_hook = run_hook


def before_scenario(*args, **kwargs):
    warnings.warn("DEPRECATED: This function is no longer needed.",
                  stacklevel=2)


def after_scenario(*args, **kwargs):
    warnings.warn("DEPRECATED: This function is no longer needed.",
                  stacklevel=2)
