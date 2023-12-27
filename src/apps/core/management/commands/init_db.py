from typing import Any
import faker
import random

from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model


User = get_user_model()

faker = faker.Faker()


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("quantity", help="Number of items per model", default=10)
        return super().add_arguments(parser)

    def handle(self, *args: Any, **options: Any) -> str | None:
        print(options.get("quantity"))

        self.stdout.write(
            self.style.SUCCESS(f"Creating elements for the database."),
        )

    def create_customers_data(self):
        """Create fake customer data"""

    def craete_orders_data(self):
        """Create data for order and orderitems"""

    def create_users_data(self, quantity):
        """Create data for users"""
        for _ in range(quantity):
            user = User.objects.create(
                username=faker.user_name(),
                email=faker.email(),
                first_name=faker.first_name(),
                last_name=faker.last_name(),
            )
            password = faker.password()
            user.set_password(password)
            user.save()
