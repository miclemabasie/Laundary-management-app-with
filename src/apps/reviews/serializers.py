from rest_framework import serializers

from .models import Review


class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ["shop", "rating", "comment"]


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ["user", "shop", "rating", "comment"]
