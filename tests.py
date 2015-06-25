"""
Test suite for behave-django.  See features folder for implementation.
Run it by

- ``python setup.py -q test -v`` or
- ``python manage.py test`` or
- ``python tests.py`` (preferred) or
- ``py.test -v`` or ``py.test -q``
"""
from os import linesep as LF
from subprocess import PIPE, Popen
import unittest


def run_silently(command):
    """Run a shell command and return both exit_status and console output."""
    command_args = command.split()
    process = Popen(command_args, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    stdout, stderr = process.communicate()
    output = (stdout + LF + stderr).strip()
    return process.returncode, output


class BehaveDjangoTestCase(unittest.TestCase):
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

    def test_dont_create_db_with_option_dryrun(self):
        exit_status, output = run_silently(
            'python manage.py behave --dry-run')
        assert exit_status == 0
        # TODO: test whether test database is created

    def test_dont_create_db_with_option_useexistingdb(self):
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
