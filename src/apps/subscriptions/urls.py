from django.urls import path
from . import views

app_name = "subscriptions"

urlpatterns = [
    path("", views.list_subscriptions, name="list-subscription"),
    path("create", views.create_subscription, name="create-subscription")
]