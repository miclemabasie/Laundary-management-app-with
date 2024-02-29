from django.urls import path
from . import views

app_name = "orders"


urlpatterns = [
    path("", views.order_list_view, name="order-list"),
    path("<str:transaction_id>", views.order_detail_view, name="order-detail"),
    path("create/<str:shop_id>", views.create_order_view, name="order-create"),
    path("update/<str:transaction_id>/", views.update_order_view, name="order-update"),
    path("delete/<str:transaction_id>/", views.delete_order_view, name="order-delete"),
]
