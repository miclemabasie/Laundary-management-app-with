# Generated by Django 5.0 on 2024-01-01 09:12

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("customers", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "transaction_id",
                    models.CharField(default=True, max_length=15, null=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("NEW", "New"),
                            ("InProgress", "InProgress"),
                            ("Completed", "Completed"),
                            ("Collected", "Collected"),
                        ],
                        default="NEW",
                        max_length=30,
                        verbose_name="Order Status",
                    ),
                ),
                (
                    "total_price",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=10,
                        verbose_name="Total Order Price",
                    ),
                ),
                (
                    "validated",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="orders",
                        to="customers.customer",
                    ),
                ),
                (
                    "sales_man",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="orders_performed",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "item_type",
                    models.CharField(max_length=50, verbose_name="Item Name"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Item Description"
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(blank=True, default=1, null=True),
                ),
                (
                    "price_per_item",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0.0,
                        max_digits=10,
                        null=True,
                        verbose_name="Price Per Item",
                    ),
                ),
                (
                    "total_price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0.0,
                        max_digits=10,
                        null=True,
                        verbose_name="Total Orderitem Price",
                    ),
                ),
                ("special_instructions", models.TextField(blank=True, null=True)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orderitems",
                        to="orders.order",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
