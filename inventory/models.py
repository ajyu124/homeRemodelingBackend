from django.db import models
from django.utils import timezone

class InventoryCategory(models.Model):
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically populated on creation
    last_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description
    
    def save(self, *args, **kwargs):
        self.last_modified = timezone.now()
        return super().save(*args, **kwargs)


class InventoryDetail(models.Model):
    item = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255, null=True, blank=True)
    price_per_unit = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(InventoryCategory, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically populated on creation
    last_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.item
    
    def save(self, *args, **kwargs):
        self.last_modified = timezone.now()
        return super().save(*args, **kwargs)
