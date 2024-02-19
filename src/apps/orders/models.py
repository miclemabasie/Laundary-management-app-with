import uuid

from collections.abc import Iterable
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel
from django.contrib.auth import get_user_model
from decimal import Decimal
from apps.customers.models import Customer
from apps.shop.models import Shop

User = get_user_model()


class OrderSatus(models.TextChoices):
    NEW = "NEW", _("New")
    INPROGRESS = "InProgress", _("InProgress")
    COMPLETED = "Completed", _("Completed")
    COLLECTED = "Collected", _("Collected")


class Order(TimeStampedUUIDModel):
    sales_man = models.ForeignKey(
        User,
        related_name="orders_performed",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    shop = models.ForeignKey(Shop, related_name="shops", on_delete=models.CASCADE)
    transaction_id = models.CharField(null=True, default=True, max_length=15)
    customer = models.ForeignKey(
        Customer, related_name="orders", on_delete=models.SET_NULL, null=True
    )
    status = models.CharField(
        verbose_name=_("Order Status"),
        max_length=30,
        choices=OrderSatus.choices,
        default=OrderSatus.NEW,
    )
    total_price = models.DecimalField(
        verbose_name=_("Total Order Price"),
        max_digits=10,
        decimal_places=2,
        default=0.0,
    )
    validated = models.BooleanField(null=True, blank=True, default=False)

    def save(self, *a, **kw) -> None:
        self.transaction_id = str(uuid.uuid4())[-12:]
        # get all orderitems for this order
        print("calling the order save########")
        if self.validated:
            order_items = OrderItem.objects.filter(order__pkid=self.pkid)
            if len(order_items) > 0:
                for order_item in order_items:
                    # Get the total cost of orderitems -> (cost_per_item * quantity)
                    self.total_price = Decimal(self.total_price) + Decimal(
                        order_item.total_price
                    )
        return super().save(*a, **kw)


class OrderItem(TimeStampedUUIDModel):
    order = models.ForeignKey(
        Order, related_name="orderitems", on_delete=models.CASCADE
    )
    item_type = models.CharField(verbose_name=_("Item Name"), max_length=50)
    description = models.TextField(
        verbose_name=_("Item Description"), null=True, blank=True
    )
    quantity = models.PositiveIntegerField(null=True, blank=True, default=1)
    price_per_item = models.DecimalField(
        verbose_name=_("Price Per Item"),
        max_digits=10,
        decimal_places=2,
        default=0.0,
        null=True,
        blank=True,
    )
    total_price = models.DecimalField(
        verbose_name=_("Total Orderitem Price"),
        max_digits=10,
        decimal_places=2,
        default=0.0,
        null=True,
        blank=True,
    )
    special_instructions = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"OrderItem -> {self.item_type} part of orderID: {self.order.pkid}"

    def save(self, *a, **kw) -> None:
        self.transaction_id = str(uuid.uuid4())[-12:]
        # get all orderitems for this order
        self.total_price = self.quantity * self.price_per_item
        return super().save(*a, **kw)
