from django.urls import path
from .views import *


app_name = "customers"


urlpatterns = [
    path("", customer_list_view, name="customer-list"),
]
