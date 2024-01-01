from django.urls import path
from . import views

app_name = "orders"


urlpatterns = [
    path("", views.order_list_view, name='order-list')
]