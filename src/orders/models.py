from django.db import models
from django.contrib.auth import get_user_model
from customers.models import Customer
from django.utils.translation import gettext_lazy as _

User = get_user_model()

ORDER_STATUSES = (
    ("new", "New"),
    ("inprocess", "In Progress"),
    ("completed", "Completed"),
    ("taken", "Taken"),
)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, verbose_name=_("Order Status"), choices=ORDER_STATUSES)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=_("Date created"))
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name=_("Date Updated"))

    def __str__(self):
        return f"Order No. {self.id} by {self.customer.name}"

    def is_complete(self):
        """
        Returns True or false depending on whether or not an 
        Order is complete
        """

    