from django.db import models
from django.contrib.auth import get_user_model
from apps.subscriptions.models import Subscription
from apps.common.models import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Shop(TimeStampedUUIDModel):
    user = models.ForeignKey(User, related_name="shop", on_delete=models.CASCADE)
    subscription = models.OneToOneField(
        Subscription, related_name="shop", on_delete=models.SET_NULL, blank=True, null=True
    )
    shop_name = models.CharField(
        verbose_name=_("Shop Name"), max_length=200, unique=True, blank=True, null=True
    )
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    Location = models.CharField(verbose_name=_("Loaction"), max_length=200, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Shop-{self.shop_name}"


class StaffMember(TimeStampedUUIDModel):
    STAFF_ROLES = (
        (1, "1 - Poor"),
        (2, "2 - Below Average"),
        (3, "3 - Average"),
        (4, "4 - Good"),
        (5, "5 - Excellent"),
    )
    shop = models.ForeignKey(
        Shop, related_name="staff_members", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(
        verbose_name=_("Staff Role"), max_length=20, choices=STAFF_ROLES
    )

    def __str__(self):
        return f"{self.user.username} staff for {self.shop.name}"
