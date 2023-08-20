from django.db import models

class InventoryDetail(models.Model):
    item = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.item
