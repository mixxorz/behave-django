from __future__ import absolute_import
from optparse import make_option
import sys

from behave.configuration import options as behave_options
from behave.runner import ModelRunner
from behave.__main__ import main as behave_main
from django.core.management.base import BaseCommand

from behave_django.runner import (BehaviorDrivenTestRunner,
                                  ExistingDatabaseTestRunner)


def get_new_options():
    return [
        make_option(
            '--use-existing-database',
            action='store_true',
            default=False,
            help="Don't create a test database. USE AT YOUR OWN RISK!",
        ),
    ]


def get_behave_options():
    new_options = get_new_options()

    conflicts = [
        '--no-color',
        '--version'
    ]

    for fixed, keywords in behave_options:
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


def get_behave_args():
    """Remove command line arguments not accepted by behave."""
    options = sys.argv[2:]
    return [opt for opt in options if opt not in get_new_options()]


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


class Command(BaseCommand):
    help = 'Runs behave tests'
    option_list = BaseCommand.option_list + get_behave_options()

    def handle(self, *args, **options):
        # Configure django environment
        if options['dry_run'] or options['use_existing_database']:
            django_test_runner = ExistingDatabaseTestRunner()
        else:
            django_test_runner = BehaviorDrivenTestRunner()
        django_test_runner.setup_test_environment()
        old_config = django_test_runner.setup_databases()

        # Run Behave tests
        monkey_patch_behave(django_test_runner)
        return_code = behave_main(args=get_behave_args())

        # Teardown django environment
        django_test_runner.teardown_databases(old_config)
        django_test_runner.teardown_test_environment()

        if return_code != 0:
            sys.exit(return_code)
