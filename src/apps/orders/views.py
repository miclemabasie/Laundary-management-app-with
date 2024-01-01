from django.shortcuts import render
from rest_framework import permissions, authentication
from rest_framework.response import Response
from .models import Order, OrderItem
from rest_framework.decorators import api_view, permission_classes
from .serializers import OrderItemSerializers, OrderSerializer

@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def order_list_view(request):

    # 
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    namespaced_data={"orders": serializer.data}
    return Response(namespaced_data)



@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def orderitem_list_view(request):

    # 
    orders = OrderItem.objects.all()
    serializer = OrderItemSerializers(orders, many=True)
    namespaced_data={"orders": serializer.data}
    return Response(namespaced_data)

