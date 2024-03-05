from django.db import models
from apps.common.models import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _
from apps.shop.models import Shop
from apps.subscriptions.models import Subscription


class Image(TimeStampedUUIDModel):
    gallery = models.OneToOneField(
        "Gallery",
        related_name="images",
        on_delete=models.CASCADE,
        verbose_name="Gallery",
    )
    name = models.CharField(
        verbose_name=_("Image Name"), max_length=200, blank=True, null=True
    )
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    image = models.ImageField(verbose_name=_("Gallery Photo"), upload_to="galleries")

    def save(self, *a, **kw):
        # Check if gallery is reached max photo size before adding any other iamge
        if not self.gallery.is_full:
            self.gallery.current_size += 1
            if self.gallery.current_size == self.gallery.max_photos:
                self.gallery.is_full = True
        return super().save(*a, **kw)


class Gallery(TimeStampedUUIDModel):
    shop = models.OneToOneField(Shop, related_name="gallery", on_delete=models.CASCADE)
    max_photos = models.PositiveIntegerField(default=0)
    current_size = models.PositiveIntegerField(default=0, blank=True, null=True)
    is_full = models.BooleanField(default=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Get subscription related to the current shop
        subscription = Subscription.objects.filter(shop=self.shop)
        # Check the type of plan currently associated to the shop
        # And set the max number of photos that can be uploaded to the gallery
        if subscription.plan_type == "basic":
            self.max_photos = 10
        elif subscription.plan_type == "standard":
            self.max_photos == 200
        elif subscription.plan_type == "premium":
            self.max_photos = 500
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Gallery - {self.shop.shop_name}"
