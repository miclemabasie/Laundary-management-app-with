from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializers(serializers.ModelSerializer):


    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Order
        fields = [
            "sales_man", "customer", "transaction_id", "status", "total_price", "validated", "created_at", "updated_at", "items"
        ]

    def get_items(self, obj):
        order_items = OrderItem.objects.filter(order__transaction_id=obj.transaction_id)
        serializer = OrderItemSerializers(order_items, many=True)
        return serializer.data

