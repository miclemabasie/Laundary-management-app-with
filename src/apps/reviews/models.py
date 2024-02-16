from django.db import models
from django.contrib.auth import get_user_model
from apps.shop.models import Shop
from apps.common.models import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Review(TimeStampedUUIDModel):
    RATING_CHOICES = (
        (1, '1 - Poor'),
        (2, '2 - Below Average'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent')
    )
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()


    class Meta:
        unique_together = ["user", "shop"]

    def __str__(self):
        return f"{self.user.username} - {self.shop.shop_name} Review"