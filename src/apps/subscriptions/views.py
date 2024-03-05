from django.shortcuts import get_object_or_404
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
    if request.method == "POST":
        # Get the data from the request
        data = request.data

        plan_type = data["plan_type"]
        user_id = data["shop_owner"]

        # Check plan type is valid
        valid_plans = ["basic", "standard", "premium"]
        if plan_type not in valid_plans:
            return Response(
                {
                    "error": "Invalid Plan, valid plans include, [basic, standard, premium]"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if user exist, since the system just takes in the userid, any number could be sent
        try:
            user_instance = get_object_or_404(User, pkid=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User with id not found"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Check if user already has a current subsciption
        subscription_exists = Subscription.objects.filter(
            shop_owner=user_id, plan_type=plan_type
        )
        if subscription_exists.exists():
            return Response(
                {"error": "Current User already has a subscription with same plan"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if user already has any form of subscriptioin
        subscription_exists = Subscription.objects.filter(shop_owner=user_id)
        if subscription_exists.exists():
            return Response(
                {
                    "error": "user can not switch subscriptions on this route, to upgrade your subscription, go to http://localhost:8000/api/v1/subscriptions/upgrade/"
                }
            )

        serializer = SubscriptionCreateSerailizer(data=data)
        if serializer.is_valid():
            # serializer.save()
            # perform payment
            # if payment is successful then:
            # save the serializer
            print("Performing payment...")
            serializer.save()
            subscription = Subscription.objects.get(shop_owner=user_id)
            # Create shop for this
            shop = Shop.objects.create(
                user=User.objects.get(pkid=user_id),
                subscription=subscription,
            )
            shop.save()
            subscription.is_active = True
            subscription.save()
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "something went wrong!"})
    else:
        return Response(
            {"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def list_subscriptions(request, *args, **kwargs):
    queryset = Subscription.objects.all()

    serializer = SubscriptionListSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def user_subscription_details(request):
    user = request.user
    subscription = Subscription.objects.filter(shop_owner=user)
    if subscription.exists():
        subscription = subscription.first()
        serializer = SubscriptionListSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(
            {"error": "Current logged in user has no subscription available"}
        )
