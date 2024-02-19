from django.shortcuts import render
from .models import Subscription
from .serializers import SubscriptionListSerializer
from rest_framework.generics import ListAPIView



class SerializerListAPIView(ListAPIView):
    queryset = Subscription.objects.all()

    serializer_class = SubscriptionListSerializer
