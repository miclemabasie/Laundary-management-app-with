# Generated by Django 3.2.7 on 2024-02-27 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20240220_0034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='Location',
            new_name='location',
        ),
    ]
