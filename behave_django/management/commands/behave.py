from __future__ import absolute_import
import os

from behave.configuration import Configuration
from behave.runner import Runner
from django.conf import settings
from django.core.management.base import BaseCommand
from django.test.runner import DiscoverRunner


class Command(BaseCommand):
    args = '<app_name app_name ...>'
    help = 'Runs behave tests'

    def handle(self, *args, **options):
        # Configure Behave
        configuration = Configuration()
        if settings.BEHAVE_FEATURES:
            configuration.paths = [x for x in settings.BEHAVE_FEATURES]
        else:
            configuration.paths = [os.path.join(settings.BASE_DIR, 'features')]
        configuration.format = ['pretty']

        # Configure django environment
        django_test_runner = DiscoverRunner()
        django_test_runner.setup_test_environment()
        old_config = django_test_runner.setup_databases()

        # Run Behave tests
        runner = Runner(configuration)
        runner.run()

        # Teardown django environment
        django_test_runner.teardown_databases(old_config)
        django_test_runner.teardown_test_environment()
