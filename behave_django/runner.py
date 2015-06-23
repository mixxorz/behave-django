try:
    from django.test.runner import DiscoverRunner
except ImportError:
    from django.test.simple import DjangoTestSuiteRunner as DiscoverRunner

from behave_django.environment import BehaveHooksMixin
from behave_django.testcase import (BehaviorDrivenTestCase,
                                    ExistingDatabaseTestCase)


class BehaviorDrivenTestRunner(DiscoverRunner, BehaveHooksMixin):
    testcase_class = BehaviorDrivenTestCase


class ExistingDatabaseTestRunner(DiscoverRunner, BehaveHooksMixin):
    testcase_class = ExistingDatabaseTestCase

    def setup_databases(*args, **kwargs):
        pass

    def teardown_databases(*args, **kwargs):
        pass
