from django.db import models

# Create your models here.


class Car(models.Model):
    """Model definition for Car."""

    name = models.CharField(verbose_name="Name")

    class Meta:
        """Meta definition for Car."""

        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        """Unicode representation of Car."""

        pass
