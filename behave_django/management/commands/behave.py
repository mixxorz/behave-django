from __future__ import absolute_import
from optparse import make_option
import sys

from behave.configuration import options
from behave.__main__ import main as behave_main
from django.core.management.base import BaseCommand

from behave_django.runner import BehaveDjangoTestRunner


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
        # Configure django environment
        django_test_runner = BehaveDjangoTestRunner()
        django_test_runner.setup_test_environment()
        old_config = django_test_runner.setup_databases()

        # Run Behave tests
        return_code = behave_main(args=sys.argv[2:])

        # Teardown django environment
        django_test_runner.teardown_databases(old_config)
        django_test_runner.teardown_test_environment()

        if return_code != 0:
            sys.exit(return_code)
