from django.shortcuts import render
from .serializers import ShopListSerializer, ShopUpdateSerializer
from .models import Shop
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(["GET"])
def list_all_shop_view(request):
    """
    List all laundary shops on the platform, this view can be accessed by all user 
    both authenticated and unauthenticated users
    """
    
    queryset = Shop.objects.all()    
    serializer = ShopListSerializer(queryset, many=True, context={"request": request})
    print("this is a response")

    print(serializer.data)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_shop_detial(request, shop_id):
    shop = Shop.objects.filter(shop_id=shop_id)
    if shop.exists():
        shop_instance = shop.first()
        serializer = ShopListSerializer(shop_instance, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Shop not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
@permission_classes([permissions.IsAuthenticated])
def update_shop_information(request, shop_id):

    shop = Shop.objects.filter(shop_id=shop_id)
    shop_instance = shop.first()
    data = request.data
    if shop.exists():
        print("inside")
        serializer = ShopUpdateSerializer(shop_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "shop has been successfuly updated."})
        else:
            print(serializer.errors)
        return Response({"message": "working on it."})
    else:
        return Response({"error": "Shop not found"}, status=status.HTTP_404_NOT_FOUND)
    