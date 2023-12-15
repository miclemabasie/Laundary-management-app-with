from django.db import models

from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    name = models.CharField(verbose_name=_("Customer Name"), max_length=50)
    email = models.EmailField(verbose_name=_("Customer Email"), max_length=254)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+237680672888"
    )
    address = models.CharField(verbose_name=_("Customer Address"), max_length=200)

    def get_oders(self):
        """Get all the oders placed by this customer"""
        pass

    def get_orders_in_progress(self):
        """Get all the uncompleted orders for this customers"""
        pass

    def get_orders_done(self):
        """Get all the orders that are done but not collected"""
        pass

    def get_orders_collected(self):
        """Get all the orders that have been collected"""
        pass
