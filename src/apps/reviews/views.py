from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.shop.models import Shop

from .models import Review
from .serializers import ReviewCreateSerializer, ReviewListSerializer

# Attach review to all shops


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_review(request):
    data = request.data

    print(data["shop"])

    # Check if shop exist
    shop = Shop.objects.filter(pkid=data["shop"])
    print(shop)
    if shop.exists():
        shop = shop.first()
    else:
        return Response(
            {"error": "Shop with given id not found."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Check rating is between 1 and 5
    if data["rating"] < 1 or data["rating"] > 5:
        return Response({"error": "Invalid rating"}, status=status.HTTP_400_BAD_REQUEST)

    # Check if the current user already has a rating for the same shop
    rating = Review.objects.filter(user=request.user, shop=shop)
    if rating.exists():
        return Response(
            {"error": "User already has a rating for the given shop."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Create review
    review_create = {
        "user": request.user,
        "shop": shop,
        "rating": data["rating"],
        "comment": data["comment"],
    }

    review_create_serializer = {
        "user": request.user,
        "shop": shop.pkid,
        "rating": data["rating"],
        "comment": data["comment"],
    }

    print("user is: ", review_create_serializer["user"])
    serializer = ReviewCreateSerializer(data=review_create_serializer)
    if serializer.is_valid():
        review = Review.objects.create(**review_create)
        review.save()

    else:
        print(serializer.errors)
        return Response(
            {"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST
        )

    review = ReviewListSerializer(review)
    return Response({"message": review.data}, status=status.HTTP_201_CREATED)
