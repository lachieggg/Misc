from django.core.management.base import BaseCommand
from pos.interfaces.cli import CLI


class Command(BaseCommand):
    help = "Process restaurant orders via CLI"

    def handle(self, *args, **options):
        try:
            CLI().run()
        except KeyboardInterrupt:
            self.stdout.write("\n\nOrder cancelled.")
