from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Customer Name"))
    email = models.EmailField(verbose_name=_("Email"))
    phone = models.CharField(max_length=12, verbose_name=_("Phone"))
    address = models.CharField(max_length=100, verbose_name=_("Address"))


    def __str__(self):
        return f"{self.name}"

    def get_all_order(self):
        """ 
        Get all the orders ever submited by a particular customer
        """
        pass

    def get_current_order(self):
        """
        Gets all the orders owned by this customers at the moment
        """
        pass

    def has_active_order(self):
        """
        Returns true of false depending whether the customer has 
        an active order or not.
        """
        pass