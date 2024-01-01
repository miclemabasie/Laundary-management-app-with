from rest_framework import serializers
from .models import Customer
from apps.orders.models import Order, OrderItem
from django.forms import model_to_dict
from apps.orders.serializers import OrderSerializer


class CustomerSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ["pkid", "name", "email", "phone_number", "address", "orders"]

    def get_orders(self, obj):
        orders = Order.objects.filter(customer__name=obj.name)
        serializer = OrderSerializer(orders, many=True)
        return serializer.data
