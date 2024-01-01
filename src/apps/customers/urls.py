from django.urls import path
from . import views


app_name = "customers"


urlpatterns = [
    path("", views.customer_list_view, name="customer-list"),
    path("create/", views.customer_create_view, name="customer-create"),
    path("<str:pkid>/", views.customer_detail_view, name="customer-detail"),
    path("update/<str:pkid>/", views.customer_update_view, name="customer-update"),
    path("delete/<str:pkid>/", views.customer_delete_view, name="customer-delete"),
]    
