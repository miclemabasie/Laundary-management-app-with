from django.urls import path
from . import views

app_name = "subscriptions"

urlpatterns = [
    path("", views.list_subscriptions, name="list-subscription"),
    path("subscribe", views.create_subscription, name="create-subscription"),
    path("subscription", views.user_subscription_details, name="get-user-subscription")
]