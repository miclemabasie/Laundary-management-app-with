from rest_framework import serializers
from .models import Shop



class ShopListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = [
            "user",
            "shop_name",
            "description", 
            "location",
            "is_verified"
        ]