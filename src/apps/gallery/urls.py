from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_gallery_view, name="create-gallery"),
    path("create/image", views.create_gallery_image_view, name="create-image"),
    path("images/", views.list_image_item_view, name="list-images"),
    path("image/delete/<str:image_id>/", views.delete_gallery_image_item, name="delete-image"),
]