from __future__ import absolute_import
from optparse import make_option
import os

from behave.configuration import Configuration, options
from behave.runner import Runner
from django.conf import settings
from django.core.management.base import BaseCommand
from django.test.runner import DiscoverRunner


def get_behave_options():
    new_options = []

    conflicts = [
        '--no-color',
        '--version'
    ]

    for fixed, keywords in options:
        long_option = None
        for option in fixed:
            if option.startswith("--"):
                long_option = option
                break

        # Do not add conflicting options
        if long_option in conflicts:
            continue

        if long_option:
            # type isn't a valid keyword for make_option
            if hasattr(keywords.get('type'), '__call__'):
                del keywords['type']
            # config_help isn't a valid keyword for make_option
            if 'config_help' in keywords:
                del keywords['config_help']

            new_options.append(
                make_option(long_option, **keywords)
            )
    return tuple(new_options)


class Command(BaseCommand):
    help = 'Runs behave tests'
    option_list = BaseCommand.option_list + get_behave_options()

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
