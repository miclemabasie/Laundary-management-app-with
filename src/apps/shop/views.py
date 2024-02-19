from django.shortcuts import render
from .serializers import ShopListSerializer
from .models import Shop
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListAPIView


class ListShopAPIView(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopListSerializer