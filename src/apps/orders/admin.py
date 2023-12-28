from django.contrib import admin
from .models import Order, OrderItem


class OrderItemIinline(admin.TabularInline):
    model = OrderItem
    fields = ["order", "item_type", "quantity", "price_per_item", "total_price"]
    verbose_name_plural = "Order Items"
    can_delete = False


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "transaction_id",
        "sales_man",
        "customer",
        "status",
        "total_price",
        "status",
        "validated",
    ]
    inlines = [OrderItemIinline]


admin.site.register(Order, OrderAdmin)
