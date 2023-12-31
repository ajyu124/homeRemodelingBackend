# Generated by Django 4.2.3 on 2023-08-18 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_remove_productdetail_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=255)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_email', models.CharField(blank=True, max_length=255, null=True)),
                ('product_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.productdetail')),
            ],
        ),
    ]
