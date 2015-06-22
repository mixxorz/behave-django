try:
    from django.test.runner import DiscoverRunner
except ImportError:
    from django.test.simple import DjangoTestSuiteRunner as DiscoverRunner

from django.core.management import call_command

try:
    from django.shortcuts import resolve_url
except ImportError:
    # support Django 1.4, which has no resolve_url() yet
    from django.shortcuts import redirect

    resolve_url = lambda to, *args, **kwargs: \
        redirect(to, *args, **kwargs)['Location']

from behave_django.testcase import (BehaviorDrivenTestCase,
                                    ExistingDatabaseTestCase)


class BehaviorDrivenTestRunner(DiscoverRunner):
    testcase_class = BehaviorDrivenTestCase

    def before_scenario(self, context):
        context.test = self.testcase_class()
        context.test.setUpClass()
        context.test()

        context.base_url = context.test.live_server_url

        def get_url(to=None, *args, **kwargs):
            return context.base_url + (
                resolve_url(to, *args, **kwargs) if to else '')

        context.get_url = get_url

    def load_fixtures(self, context):
        if getattr(context, 'fixtures', None):
            call_command('loaddata', *context.fixtures, verbosity=0)

    def after_scenario(self, context):
        context.test.tearDownClass()
        del context.test


class ExistingDatabaseTestRunner(BehaviorDrivenTestRunner):
    testcase_class = ExistingDatabaseTestCase

    def setup_databases(*args, **kwargs):
        pass

    def teardown_databases(*args, **kwargs):
        pass


def get_runner(options):
    """Yield a test runner honoring the user supplied command line options."""
    runner_class = ExistingDatabaseTestRunner \
        if options['dry_run'] or options['use_existing_database'] \
        else DiscoverRunner

    return runner_class()
