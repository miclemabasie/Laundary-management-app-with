from django.contrib import admin

from apps.orders.models import Order, OrderItem

from .models import Customer

# class OrderInline(admin.TabularInline):
#     model = Order
#     fields = ["transaction_id", "status", "total_price", "validated"]
#     verbose_name = "Orders related to this customer."


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone_number", "address"]

    # inlines = [OrderInline]


admin.site.register(Customer, CustomerAdmin)
