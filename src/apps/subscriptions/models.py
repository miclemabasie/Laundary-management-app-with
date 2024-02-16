from django.db import models
from apps.common.models import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Subscription(TimeStampedUUIDModel):

    PLAN_CHOICES = [
        ("basic", "Basic"),
        ("standard", "Standard"),
        ("premium", "Premium"),
    ]

    transaction_id = models.CharField(
        verbose_name=_("Transaction_id"), max_length=20, unique=True
    )
    shop_owner = models.ForeignKey(User, related_name="subscriptions", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    plan_type = models.CharField(verbose_name=_("Plan Type"), max_length=20, choices=PLAN_CHOICES)
    start_data = models.DateTimeField()
    end_data = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    
    def __str__(self):
        return f"subscription-{self.shop}"
