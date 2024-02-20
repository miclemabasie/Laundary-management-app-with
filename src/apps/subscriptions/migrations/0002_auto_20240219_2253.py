# Generated by Django 3.2.7 on 2024-02-19 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='end_data',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='start_data',
            new_name='start_date',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Transaction_id'),
        ),
    ]