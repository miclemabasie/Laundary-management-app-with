from django.shortcuts import render
from rest_framework import permissions, authentication
from rest_framework.response import Response
from .models import Order, OrderItem
from rest_framework.decorators import api_view, permission_classes
from .serializers import OrderItemSerializers, OrderSerializer, OrderCreateSerializer
from django.contrib.auth import get_user_model
from apps.customers.models import Customer
from apps.shop.models import Shop

User = get_user_model()


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def order_list_view(request, shop_id):
    #
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    namespaced_data = {"orders": serializer.data}
    return Response(namespaced_data)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def order_detail_view(request, transaction_id, shop_id):
    orders = Order.objects.get(transaction_id=transaction_id)
    serializer = OrderSerializer(orders)
    print(request.headers)
    namespaced_data = {"orders": serializer.data}
    return Response(namespaced_data)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def orderitem_list_view(request, shop_id):
    #
    orders = OrderItem.objects.all()
    serializer = OrderItemSerializers(orders, many=True)
    namespaced_data = {"orders": serializer.data}
    return Response(namespaced_data)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_order_view(request, shop_id, *a, **kw):
    data = request.data

    # extract thet order items from the request
    orderitems = data["orderitems"]

    # Add some useful data to the response object

    meta_data = {}
    meta_data["new_customer"] = False

    # Get shop which order belongs to ...
    shops = Shop.objects.filter(shop_id=shop_id)
    if shops.exists() and len(shops) == 1:
        shop = shops.first()
    else:
        return Response({"error": "shop with given ID not found"})

    # to be fixed / get a user from the database
    # for now, we are just getting the shop owner and assigning the order to him
    user = User.objects.filter(shop=shop)
    if user.exists():
        user = user.first()

    # get customer based on id
    customer, created = Customer.objects.get_or_create(
        name=data["customer"], phone_number=data["phone"]
    )
    # Check if the the customer was just created or has been in the system
    # Then let the shop owner know if this was a new user
    # by adding "new_customer" as metadata to the response
    # Which could be used to do custome things.
    if created:
        meta_data["new_customer"] = True

    order_create_data = {
        "sales_man": user,
        "customer": customer,
        "status": data["status"],
    }

    # Create a new order for a particular shop in the database
    order = Order.objects.create(**order_create_data, shop=shop)

    # Add all the order items to the created order
    # By attaching the order pkid to every orderitem
    for orderitem in orderitems:
        orderitem["order"] = order.pkid
        orderitem_serializer = OrderItemSerializers(data=orderitem)
        if orderitem_serializer.is_valid():
            orderitem_serializer.save()
        else:
            return Response({"error": orderitem_serializer.errors})

    # Validate the order instance
    # This is done to allow the price transaction inside the save method to now take place
    # since all the orderitems have now been added to the created order
    order.validated = True
    order.save()

    # return serializer
    order_serializer = OrderSerializer(order)
    namedspaced_response = {"meta_data": meta_data, "order": order_serializer.data}
    return Response(namedspaced_response)


@api_view(["PATCH"])
@permission_classes([permissions.IsAuthenticated])
def update_order_view(request, transaction_id, *a, **kw):
    try:
        order = Order.objects.get(transaction_id=transaction_id)
    except Order.DoesNotExist:
        return Response({"error": "Order with this id does not exist!"})
    serializer = OrderSerializer(instance=order, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def delete_order_view(reqeust, transaction_id, *a, **kw):
    try:
        order = Order.objects.get(transaction_id=transaction_id)
    except Order.DoesNotExist:
        return Response({"error": "Order with this id does not exist!"})

    order.delete()
    return Response({"success": "Order has been successfully deleted."})
