try:
    from django.contrib.staticfiles.testing import StaticLiveServerTestCase
except ImportError:
    from django.test import LiveServerTestCase as StaticLiveServerTestCase


class BehaveDjangoTestCase(StaticLiveServerTestCase):

    def runTest(*args, **kwargs):
        pass
