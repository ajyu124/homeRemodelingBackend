# Generated by Django 4.2.3 on 2023-08-25 06:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_productdetail_image_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetail',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
