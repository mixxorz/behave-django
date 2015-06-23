"""
Test suite for behave-django.  See features folder for implementation.
Run it by

- ``python setup.py -q test -v`` or
- ``python manage.py test`` or
- ``python tests.py`` (preferred)
"""
import os
import subprocess
import unittest


def run_silently(command):
    FNULL = open(os.devnull, 'w')
    exit_code = subprocess.call(
        command, stdout=FNULL, stderr=subprocess.STDOUT)
    FNULL.close()
    return exit_code


class BehaveDjangoTestCase(unittest.TestCase):
    def test_command_should_exit_zero_if_passing(self):
        self.assertEqual(0, run_silently(
            ['python', 'manage.py', 'behave', '--tags', '~@failing']
        ))

    def test_command_should_exit_nonzero_if_failing(self):
        self.assertNotEqual(0, run_silently(
            ['python', 'manage.py', 'behave', '--tags', '@failing'],
        ))

    def test_flake8(self):
        self.assertEqual(0, run_silently('flake8'))


if __name__ == '__main__':
    unittest.main()
