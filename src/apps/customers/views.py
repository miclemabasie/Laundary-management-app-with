from django.shortcuts import render
from rest_framework import permissions, authentication
from .models import Customer
from apps.orders.models import Order, OrderItem
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response
from .serializers import CustomerSerializer
from rest_framework.generics import ListAPIView

from rest_framework import status

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def customer_list_view(request):
    customers = Customer.objects.all()

    serializer = CustomerSerializer(customers, many=True)
    namespaced_data = {"Customers": serializer.data}
    return Response(namespaced_data)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def customer_detail_view(request, pkid, *a, **kw):
    try:
        customer = Customer.objects.get(pkid=pkid)
    except Customer.DoesNotExist:
        return Response({"error": "Customer with does not exist"}, status.HTTP_400_BAD_REQUEST)
    
    serializer = CustomerSerializer(customer)

    namespaced_response = {"customer": serializer.data}
    return Response(namespaced_response, status=status.HTTP_200_OK)

@api_view(["PATCH"])
@permission_classes([permissions.IsAuthenticated])
def customer_update_view(request, pkid, *a, **kw):
    try:
        customer = Customer.objects.get(pkid=pkid)
    except Customer.DoesNotExist:
        return Response({"error": "Customer with does not exist"}, status.HTTP_400_BAD_REQUEST)
    serializer = CustomerSerializer(instance=customer, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": "Customer updated!"})
    return Response({"error": serializer.errors})



@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def customer_delete_view(request, pkid, *a, **kw):
    try:
        customer = Customer.objects.get(pkid=pkid)
    except Customer.DoesNotExist:
        return Response({"error": "Customer with does not exist"}, status.HTTP_400_BAD_REQUEST)
    customer.delete()
    return Response({"success": "Customer Successfully deleted"})


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def customer_create_view(request):
    data = request.data
    # Check if customer with credentials already exists
    name = data['name']
    phone = data['phone_number']
    serializer = CustomerSerializer(data=data)
    if serializer.is_valid():
        # Check customer with same info
        customer, created = Customer.objects.get_or_create(name=name, phone_number=phone)
        customer.save()
        serializer = CustomerSerializer(customer)
        if created:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

