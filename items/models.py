from django.db import models
from django.utils.translation import gettext_lazy as _
from orders.models import Order


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name=_("Item Name"))
    description = models.TextField(verbose_name=_("Item Description"))
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.order.id}"