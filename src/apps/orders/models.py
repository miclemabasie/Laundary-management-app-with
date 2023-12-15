from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel
from django.contrib.auth import get_user_model


User = get_user_model()


class OrderSatus(models.TextChoices):
    NEW = "New", _("New")
    INPROGRESS = "InProgress", _("InProgress")
    COMPLETED = "Completed", _("Completed")
    COLLECTED = "Collected", _("Collected")


class Order(TimeStampedUUIDModel):
    customer = models.ForeignKey(
        User, related_name="orders", on_delete=models.SET_NULL, null=True
    )
    status = models.CharField(
        verbose_name=_("Order Status"),
        max_length=30,
        choices=OrderSatus.choices,
        default=OrderSatus.NEW,
    )


class OrderItem(TimeStampedUUIDModel):
    order = models.ForeignKey(
        Order, related_name="orderitems", on_delete=models.CASCADE
    )
    name = models.CharField(verbose_name=_("Item Name"), max_length=50)
    description = models.TextField(
        verbose_name=_("Item Description"), null=True, blank=True
    )

    def __str__(self):
        return f"OrderItem -> {self.name} part of orderID: {self.order.pkid}"
