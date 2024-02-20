
# Generated by Django 3.2.7 on 2024-02-19 21:48
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('max_photos', models.PositiveIntegerField(default=0)),
                ('shop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='shop.shop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Image Name')),
                ('image', models.ImageField(upload_to='galleries', verbose_name='Gallery Photo')),
                ('gallery', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gallery.gallery', verbose_name='Gallery')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]