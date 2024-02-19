from django.db import models
from apps.common.models import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
import uuid
from django.utils import timezone
from datetime import timedelta

User = get_user_model()


class Subscription(TimeStampedUUIDModel):

    PLAN_CHOICES = [
        ("basic", "Basic"),
        ("standard", "Standard"),
        ("premium", "Premium"),
    ]

    shop_owner = models.ForeignKey(
        User, related_name="subscriptions", on_delete=models.CASCADE
    )
    plan_type = models.CharField(
        verbose_name=_("Plan Type"), max_length=20, choices=PLAN_CHOICES
    )
    transaction_id = models.CharField(
        verbose_name=_("Transaction_id"),
        max_length=20,
        unique=True,
        blank=True,
        null=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def save(self, *a, **kw) -> None:
        # Auto fill in the transactioni id
        self.transaction_id = str(uuid.uuid4())[-17:]
        # Calulate and save prices based on plan choice
        self.start_date = timezone.now()
        self.end_date = self.start_date + timedelta(365)
        if self.plan_type == "basic":
            self.price = 0.0
        elif self.plan_type == "standard":
            self.price = 10.0
        elif self.plan_type == "premium":
            self.price = 20.0
        self.is_active = True
        return super().save(*a, *kw)

    def __str__(self):
        return f"subscription-{self.shop}"
