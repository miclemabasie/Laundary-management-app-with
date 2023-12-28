from typing import Any
import faker
import random

from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from apps.orders.models import Order, OrderItem
from apps.customers.models import Customer


User = get_user_model()

faker = faker.Faker()


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "quantity", type=int, help="Number of items per model", default=10
        )
        return super().add_arguments(parser)

    def handle(self, *args: Any, **options: Any) -> str | None:
        print(options.get("quantity"))
        self.quantity = options.get("quantity")
        self.stdout.write(
            self.style.WARNING(f"Do not interrupt! Creating application mock data..."),
        )
        # self.create_users_data(self.quantity)
        # self.create_orders_data(self.quantity)
        self.create_customers_data(10)

    def create_customers_data(self, quantity):
        """Create fake customer data"""
        for _ in range(quantity):
            customer = Customer.objects.create(
                name=faker.name(),
                email=faker.email(),
                phone_number=faker.phone_number(),
                address=faker.address(),
            )
            customer.save()

    def create_orders_data(self, quantity):
        """Create data for order and orderitems"""
        # create an order
        for _ in range(quantity):
            order = Order.objects.create()
            # randomly get a number of order items to create
            number_order_items = random.randint(1, 5)
            for _ in range(number_order_items):
                # Create random items
                orderitem = OrderItem.objects.create(
                    order=order,
                    item_type=faker.name_nonbinary(),
                    description=faker.text(max_nb_chars=20),
                    price_per_item=faker.random_number(1, True),
                    quantity=5,
                    special_instructions=faker.text(max_nb_chars=30),
                )
                orderitem.save()
            order.validated = True
            order.save()

    def create_users_data(self, quantity):
        """Create data for users"""
        self.stdout.write(self.style.SUCCESS(f"Creating User data..."))
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
        self.stdout.write(self.style.SUCCESS(f"User Data Crated successfully"))
