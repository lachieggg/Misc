from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Order food"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="A name to greet")

    def handle(self, *args, **options):
        name = options["name"]
        self.stdout.write(self.style.SUCCESS(f"Hello, {name}!"))
