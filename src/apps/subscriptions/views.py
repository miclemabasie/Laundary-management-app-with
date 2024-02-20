from django.shortcuts import render
from .models import Subscription
from .serializers import SubscriptionListSerializer, SubscriptionCreateSerailizer
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from apps.shop.models import Shop


User = get_user_model()


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_subscription(request, *args, **kwargs):
    # Get the data from the request
    data = request.data

    plan_type = data["plan_type"]
    user = data["shop_owner"]

    serializer = SubscriptionCreateSerailizer(data=data)
    if serializer.is_valid():
        # serializer.save()
        # perform payment
        # if payment is successful then:
        # save the serializer
        print("Performing payment...")
        serializer.save()
        subscription = Subscription.objects.get(shop_owner=user)
        # Create shop for this 
        shop = Shop.objects.create(
            user = User.objects.get(pkid=user),
            subscription = subscription,
        )
        shop.save()
        return Response({"message": "success"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "something went wrong!"})
    

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def list_subscriptions(request, *args, **kwargs):
    queryset = Subscription.objects.all()

    serializer = SubscriptionListSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)