import os
import subprocess
import unittest


class BehaveDjangoTestCase(unittest.TestCase):

    def test_command_should_exit_zero_if_passing(self):
        # FNULL = open(os.devnull, 'w')
        return_code = subprocess.call(
            ['python', 'manage.py', 'behave', '--tags', '~@failing'],
            # stdout=FNULL,
            # stderr=subprocess.STDOUT,
            )
        self.assertEqual(return_code, 0)

    def test_command_should_exit_nonzero_if_failing(self):
        # FNULL = open(os.devnull, 'w')
        return_code = subprocess.call(
            ['python', 'manage.py', 'behave', '--tags', '@failing'],
            # stdout=FNULL,
            # stderr=subprocess.STDOUT,
            )
        self.assertNotEqual(return_code, 0)

if __name__ == '__main__':
    unittest.main()
