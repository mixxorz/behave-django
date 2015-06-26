"""
Test suite for behave-django.  See features folder for implementation.
Run it by

- ``python setup.py -q test -v`` or
- ``python manage.py test`` or
- ``python tests.py`` (preferred)
"""
from django.core.management import call_command
from mock import patch
from os import linesep as LF
from subprocess import PIPE, Popen
import django
import os
import unittest


def run_silently(command):
    """Run a shell command and return both exit_status and console output."""
    command_args = command.split()
    process = Popen(command_args, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    stdout, stderr = process.communicate()
    output = (stdout.decode('UTF-8') + LF +
              stderr.decode('UTF-8')).strip()
    return process.returncode, output


def run_management_command(command, *args, **kwargs):
    try:
        # required only since version 1.7
        django.setup()
    except AttributeError:
        pass
    call_command(command, *args, **kwargs)


class BehaveDjangoTestCase(unittest.TestCase):
    def setUp(self):
        # NOTE: this may potentially have side-effects, making tests pass
        # that would otherwise fail, because it *always* overrides which
        # settings module is used.
        os.environ['DJANGO_SETTINGS_MODULE'] = 'test_project.settings'

    def test_flake8(self):
        exit_status, output = run_silently('flake8')
        assert exit_status == 0

    def test_additional_management_command_options(self):
        exit_status, output = run_silently(
            'python manage.py behave --help')
        assert exit_status == 0
        assert (LF + '  --use-existing-database' + LF) in output

    def test_command_should_exit_zero_if_passing(self):
        exit_status, output = run_silently(
            'python manage.py behave --tags ~@failing')
        assert exit_status == 0

    def test_command_should_exit_nonzero_if_failing(self):
        exit_status, output = run_silently(
            'python manage.py behave --tags @failing')
        assert exit_status != 0

    @patch('behave_django.management.commands.behave.ExistingDatabaseTestRunner')  # noqa
    @patch('behave_django.management.commands.behave.behave_main', return_value=0)  # noqa
    def test_dont_create_db_with_dryrun(self, mock_existing_database_runner,
                                        mock_behave_main):
        run_management_command('behave', dry_run=True)
        mock_existing_database_runner.assert_called_with(args=[])

    def test_dont_create_db_with_useexistingdb(self):
        exit_status, output = run_silently(
            'python manage.py behave --use-existing-database'
            ' --tags ~@fail_existing_database --tags ~@failing')
        assert exit_status == 0
        exit_status, output = run_silently(
            'python manage.py behave --use-existing-database'
            ' --tags @fail_existing_database')
        assert exit_status != 0
        # TODO: test whether existing database is used


if __name__ == '__main__':
    unittest.main()
