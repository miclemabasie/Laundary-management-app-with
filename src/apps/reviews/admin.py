from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["rating", "comment", "shop"]


admin.site.register(Review, ReviewAdmin)