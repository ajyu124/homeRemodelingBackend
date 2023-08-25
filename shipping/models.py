from django.db import models
from django.utils import timezone

from product.models import ProductDetail

class ShippingDetail(models.Model):
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically populated on creation
    last_modified = models.DateTimeField(default=timezone.now)

    customer_name = models.CharField(max_length=255, null=True, blank=True)
    customer_email = models.CharField(max_length=255, null=True, blank=True)

    product_detail = models.ForeignKey(ProductDetail, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.street_address
    
    def save(self, *args, **kwargs):
        self.last_modified = timezone.now()
        return super().save(*args, **kwargs)
