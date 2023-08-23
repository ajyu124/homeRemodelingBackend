from django.db import models

class InventoryCategory(models.Model):
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.description

class InventoryDetail(models.Model):
    item = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255, null=True, blank=True)
    price_per_unit = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(InventoryCategory, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.item
