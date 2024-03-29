# Generated by Django 3.2.7 on 2024-02-19 21:48


import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shop_name', models.CharField(max_length=200, unique=True, verbose_name='Shop Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('Location', models.CharField(max_length=200, verbose_name='Loaction')),
                ('subscription', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shop', to='subscriptions.subscription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(choices=[(1, '1 - Poor'), (2, '2 - Below Average'), (3, '3 - Average'), (4, '4 - Good'), (5, '5 - Excellent')], max_length=20, verbose_name='Staff Role')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_members', to='shop.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
