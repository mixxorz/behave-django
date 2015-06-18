try:
    from django.test.runner import DiscoverRunner
except ImportError:
    from django.test.simple import DjangoTestSuiteRunner as DiscoverRunner


class ExistingDatabaseTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        pass

    def teardown_databases(self, old_config, **kwargs):
        pass


BehaveDjangoTestRunner = ExistingDatabaseTestRunner if True else DiscoverRunner
