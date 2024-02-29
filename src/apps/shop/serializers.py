from rest_framework import serializers
from .models import Shop
from django.urls import reverse
from django.http import HttpRequest


class ShopListSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='shop:shop-detail',
        lookup_field='shop_id'  
    )

    place_order_url = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Shop
        fields = [
            "user",
            "shop_name",
            "description", 
            "location",
            "is_verified",
            "shop_id",
            "logo",
            "url",
            "place_order_url",
        ]

    def __init__(self, instance=None, data=serializers.empty, context=None, **kwargs):
        # Access the request from the context
        self.request = context.get('request') if context else None

        # Your custom initialization logic here, using the request if needed

        super().__init__(instance=instance, data=data, context=context, **kwargs)

    def get_place_order_url(self, obj):
        relative_path = reverse("orders:order-create", kwargs={"shop_id": obj.shop_id})
        full_path = self.request.build_absolute_uri(relative_path)
        return full_path

class ShopUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Shop
        fields = [
            "shop_name",
            "description",
            "location",
            "logo"
        ]