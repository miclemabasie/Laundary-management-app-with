from django.db import models
from apps.common.models import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _
from apps.shop.models import Shop

class Image(TimeStampedUUIDModel):
    gallery = models.OneToOneField("Gallery", related_name="images", on_delete=models.CASCADE, verbose_name="Gallery")
    name = models.CharField(verbose_name=_("Image Name"), max_length=200)
    image = models.ImageField(
        verbose_name=_("Gallery Photo"), upload_to="galleries"
    )


class Gallery(TimeStampedUUIDModel):
    shop = models.OneToOneField(Shop, related_name="gallery", on_delete=models.CASCADE)
    max_photos = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"Gallery - {self.shop.shop_name}"