from rest_framework import serializers
from .models import Gallery, Image


class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "name",
            "description",
            "image",
        ]

class ImageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ["gallery", "image", "name", "description", "shop_id"]

class GalleryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ["shop"]




