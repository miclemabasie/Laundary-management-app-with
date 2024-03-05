from django.contrib import admin

from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["price", "transaction_id", "plan_type"]


admin.site.register(Subscription, SubscriptionAdmin)
