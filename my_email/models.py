from django.db import models

class MyEmailDetail(models.Model):
    recipient = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, null=True, blank=True)
    body = models.CharField(max_length=255, null=True, blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)  # Automatically populated on creation

    def __str__(self):
        return self.name
