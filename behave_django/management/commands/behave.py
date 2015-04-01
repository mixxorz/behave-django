from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<app_name app_name ...>'
    help = 'Runs behave tests'

    def handle(self, *args, **options):
        self.stdout.write('TODO: Run behave tests')
