# Generated by Django 4.2.3 on 2023-08-25 18:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_shippingdetail_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingdetail',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
