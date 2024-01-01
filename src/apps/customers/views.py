from django.shortcuts import render
from rest_framework import permissions, authentication
from .models import Customer
from apps.orders.models import Order, OrderItem
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .serializers import CustomerSerializer
from rest_framework.generics import ListAPIView

@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def customer_list_view(reqeust):

    customers = Customer.objects.all()

    serializer = CustomerSerializer(customers, many=True)
    namespaced_data = {"Customers": serializer.data}
    return Response(namespaced_data)


