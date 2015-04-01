from __future__ import absolute_import
import os

from behave.configuration import Configuration
from behave.runner import Runner
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<app_name app_name ...>'
    help = 'Runs behave tests'

    def handle(self, *args, **options):
        configuration = Configuration()
        configuration.paths = [os.path.join(settings.BASE_DIR, 'features')]
        configuration.format = ['pretty']
        runner = Runner(configuration)
        runner.run()
