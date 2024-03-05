from django.contrib import admin

from .models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ["user", "subscription", "shop_name", "location", "is_verified"]


admin.site.register(Shop, ShopAdmin)
