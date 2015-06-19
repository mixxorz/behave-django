try:
    from django.contrib.staticfiles.testing import StaticLiveServerTestCase
except ImportError:
    from django.test import LiveServerTestCase as StaticLiveServerTestCase


class BehaviorDrivenTestCase(StaticLiveServerTestCase):
    def runTest(*args, **kwargs):
        pass


class ExistingDatabaseTestCase(BehaviorDrivenTestCase):
    def _fixture_setup(self):
        pass

    def _fixture_teardown(self):
        pass


BehaveDjangoTestCase = ExistingDatabaseTestCase if True else BehaviorDrivenTestCase
