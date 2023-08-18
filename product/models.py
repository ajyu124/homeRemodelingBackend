from django.db import models

class ProductDetail(models.Model):
    name = models.CharField(max_length=255)
    image_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
