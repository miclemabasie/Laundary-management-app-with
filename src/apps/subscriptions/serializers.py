from rest_framework import serializers

from .models import Subscription


class SubscriptionCreateSerailizer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ["shop_owner", "plan_type"]


class SubscriptionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = [
            "shop_owner",
            "plan_type",
            "transaction_id",
            "price",
            "start_date",
            "end_date",
            "is_active",
            # Basic Plan Features
            "basic_order_tracking",
            "basic_subscription_plans",
            "basic_customer_support",
            "basic_limited_image_uploads",
            "basic_basic_email_campaigns",
            "basic_gallery_and_portfolio",
            "basic_limited_access_tutorials_guides",
            # ", Standard Plan Features
            "standard_order_tracking",
            "standard_customer_support",
            "standard_enhanced_image_uploads",
            "standard_basic_email_campaigns",
            "standard_portfolio_showcase",
            "standard_standard_industry_resources",
            "standard_webinars_training_sessions",
            # Premium Plan Features
            "premium_order_tracking",
            "premium_customer_support",
            "premium_ai_powered_insights",
            "premium_integration_with_ai_tools",
            "premium_custom_reports",
            "premium_marketing_campaigns",
            "premium_gallery_and_portfolio",
            "premium_training_and_resources",
        ]
