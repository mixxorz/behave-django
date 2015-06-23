"""
Test suite for behave-django.  See features folder for implementation.
Run it by

- ``python setup.py -q test -v`` or
- ``python manage.py test`` or
- ``python tests.py`` (preferred)
- ``py.test -q``
"""
import os
import subprocess
import unittest


def run_silently(command):
    FNULL = open(os.devnull, 'w')
    exit_status = subprocess.call(
        command, stdout=FNULL, stderr=subprocess.STDOUT)
    FNULL.close()
    return exit_status


class BehaveDjangoTestCase(unittest.TestCase):
    def test_command_should_exit_zero_if_passing(self):
        exit_status = run_silently(
            ['python', 'manage.py', 'behave', '--tags', '~@failing'])
        assert exit_status == 0

    def test_command_should_exit_nonzero_if_failing(self):
        exit_status = run_silently(
            ['python', 'manage.py', 'behave', '--tags', '@failing'])
        assert exit_status != 0

    def test_flake8(self):
        exit_status = run_silently('flake8')
        assert exit_status == 0


if __name__ == '__main__':
    unittest.main()
