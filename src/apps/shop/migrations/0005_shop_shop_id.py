# Generated by Django 3.2.7 on 2024-02-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_location_shop_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop_id',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Shop ID'),
        ),
    ]
