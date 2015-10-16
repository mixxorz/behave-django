try:
    import unittest.mock as mock
except ImportError:
    import mock

import django
import pytest

from .util import DjangoSetupMixin


class TestKeepDB(DjangoSetupMixin):

    @pytest.mark.skipif(django.VERSION < (1, 8),
                        reason="keepdb not available in Django < 1.8")
    @mock.patch('behave_django.management.commands.behave.behave_main', return_value=0)  # noqa
    @mock.patch('behave_django.management.commands.behave.BehaviorDrivenTestRunner')  # noqa
    def test_keepdb_flag_should_set_test_runner_for_keepdb(self,
                                                           mock_test_runner,
                                                           mock_behave_main):
        """Test if keepdb is properly set on the test_runner"""

        instance = mock_test_runner.return_value
        self.run_management_command('behave', keepdb=True)
        assert instance.keepdb is True
