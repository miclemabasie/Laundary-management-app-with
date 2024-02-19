from django.urls import path
from . import views

app_name = "subscriptions"

urlpatterns = [
    path("", views.SerializerListAPIView.as_view(), name="list-subscription")
]