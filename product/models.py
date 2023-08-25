from django.db import models
from django.utils import timezone

class ProductDetail(models.Model):
    name = models.CharField(max_length=255)
    image_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically populated on creation
    last_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.last_modified = timezone.now()
        return super().save(*args, **kwargs)


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/product/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
