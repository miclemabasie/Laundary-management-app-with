from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
    path("", views.list_all_shop_view, name="list-shops"),
    path("<str:shop_id>/", views.get_shop_detial, name="shop-detail"),
    path("update/<str:shop_id>/", views.update_shop_information, name="update-shop"),
]
