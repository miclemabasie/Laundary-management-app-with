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
        User, related_name="subscriptions", on_delete=models.SET_NULL, blank=True, null=True
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

    # Core features

    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    # Basic Plan Features
    basic_order_tracking = models.BooleanField(default=True)
    basic_subscription_plans = models.BooleanField(default=True)
    basic_customer_support = models.BooleanField(default=True)
    basic_limited_image_uploads = models.BooleanField(default=True)
    basic_basic_email_campaigns = models.BooleanField(default=True)
    basic_gallery_and_portfolio = models.BooleanField(default=True)
    basic_limited_access_tutorials_guides = models.BooleanField(default=True)

    # Standard Plan Features
    standard_order_tracking = models.BooleanField(default=False)
    standard_customer_support = models.BooleanField(default=False)
    standard_enhanced_image_uploads = models.BooleanField(default=False)
    standard_basic_email_campaigns = models.BooleanField(default=False)
    standard_portfolio_showcase = models.BooleanField(default=False)
    standard_standard_industry_resources = models.BooleanField(default=False)
    standard_webinars_training_sessions = models.BooleanField(default=False)

    # Premium Plan Features
    premium_order_tracking = models.BooleanField(default=False)
    premium_customer_support = models.BooleanField(default=False)
    premium_ai_powered_insights = models.BooleanField(default=False)
    premium_integration_with_ai_tools = models.BooleanField(default=False)
    premium_custom_reports = models.BooleanField(default=False)
    premium_marketing_campaigns = models.BooleanField(default=False)
    premium_gallery_and_portfolio = models.BooleanField(default=False)
    premium_training_and_resources = models.BooleanField(default=False)



    def save(self, *a, **kw) -> None:
        # Auto fill in the transactioni id
        self.transaction_id = str(uuid.uuid4())[-17:]
        # Calulate and save prices based on plan choice
        self.start_date = timezone.now()
        self.end_date = self.start_date + timedelta(365)
        if self.plan_type == "basic":
            self.price = 0.0
        elif self.plan_type == "standard":
             # Standard Plan Features
            self.standard_order_tracking = True
            self.standard_customer_support = True
            self.standard_enhanced_image_uploads = True
            self.standard_basic_email_campaigns = True
            self.standard_portfolio_showcase = True
            self.standard_standard_industry_resources = True
            self.standard_webinars_training_sessions = True
            self.price = 10.0
        elif self.plan_type == "premium":
            # standard plan features
            self.standard_order_tracking = True
            self.standard_customer_support = True
            self.standard_enhanced_image_uploads = True
            self.standard_basic_email_campaigns = True
            self.standard_portfolio_showcase = True
            self.standard_standard_industry_resources = True
            self.standard_webinars_training_sessions = True
            # Premium Plan Features
            self.premium_order_tracking = True
            self.premium_customer_support = True
            self.premium_ai_powered_insights = True
            self.premium_integration_with_ai_tools = True
            self.premium_custom_reports = True
            self.premium_marketing_campaigns = True
            self.premium_gallery_and_portfolio = True
            self.premium_training_and_resources = True
            self.price = 20.0
            
        return super().save(*a, **kw)

    def __str__(self):
        return f"subscription-{self.shop}"