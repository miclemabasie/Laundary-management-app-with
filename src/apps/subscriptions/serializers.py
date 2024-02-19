from rest_framework import serializers
from .models import Subscription


class SubscriptionCreateSerailizer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = [
            "shop_owner",
            "plan_type"         
        ]

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
            "is_active"
        ]