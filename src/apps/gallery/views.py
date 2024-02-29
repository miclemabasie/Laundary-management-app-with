from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from models import Gallery, Image
from .serializers import GalleryCreateSerializer, ImageCreateSerializer, ImageListSerializer
from apps.shop.models import Shop


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_gallery_view(request):
    data = request.data
    shop_id = data["shop"]
    # check if shop exist in the database
    shop = Shop.objects.filter(shop_id=shop_id)
    if shop.exists():
        shop = shop.first()
    else:
        return Response({"error": "Shop not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    # if shop exist then we move on to create a gallery for the specific shop

    serializer = GalleryCreateSerializer(data=data, context={"request": request})

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({"message": "Gallery successfuly created."}, status=status.HTTP_201_CREATED)
    else:
        return Response({"error": "something went wrong."})




@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_gallery_image_view(request):
    data = request.data

    # Check if gallery exist
    gallery = Gallery.objects.filter(shop=data["shop_id"])
    if gallery.exists():
        gallery = gallery.first()
        # Check if gallery has not reached max photos limit
        if gallery.is_full:
            return Response({"error": "Gallery size has been exhausted."})
    else:
        return Response({"error": "Gallery not found"}, status=status.HTTP_400_BAD_REQUEST)
    image_create_data = {
        "gallery": data["gallery"],
        "image": data["image"],
        "name": data["description"],
    }
    serializer = ImageCreateSerializer(data=image_create_data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response({"error": "somthing went wrong"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"message": "Image Item Added."}, status=status.HTTP_201_CREATED)
    


@api_view(["GET"])
def list_image_item_view(request, shop_id):
    shop = Shop.objects.filter(shop_id=shop_id)
    
    if shop.exists():
        shop = shop.first()
    else:
        return Response({"error": "Shop with id not found"}, status=status.HTTP_400_BAD_REQUEST)
    # Proceed if shop exist.
    queryset = Image.objects.filter(gallery__shop = shop_id)

    serializer = ImageListSerializer(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def delete_gallery_image_item(reqeust, image_id):
    # get image
    image = Image.objects.filter(id=image_id)
    if image.exists():
        image = image.first()
        image.delete
        return Response({"message": "image delted"}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"error": "Item not found."}, status=status.HTTP_400_BAD_REQUEST)