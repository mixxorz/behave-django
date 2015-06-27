try:
    from django.test.runner import DiscoverRunner
except ImportError:
    from django.test.simple import DjangoTestSuiteRunner as DiscoverRunner

from behave_django.environment import BehaveHooksMixin
from behave_django.testcase import (BehaviorDrivenTestCase,
                                    ExistingDatabaseTestCase)


class BehaviorDrivenTestRunner(DiscoverRunner, BehaveHooksMixin):

    """Test runner that uses the BehaviorDrivenTestCase"""
    testcase_class = BehaviorDrivenTestCase


class ExistingDatabaseTestRunner(DiscoverRunner, BehaveHooksMixin):

    """Test runner that uses the ExistingDatabaseTestCase

    This test runner nullifies Django's test database setup methods. Using this
    test runner would make your tests run with the default configured database
    in settings.py.
    """
    testcase_class = ExistingDatabaseTestCase

    def setup_databases(*args, **kwargs):
        pass

    def teardown_databases(*args, **kwargs):
        pass
