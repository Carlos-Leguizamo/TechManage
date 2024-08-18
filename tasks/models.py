# models.py
from django.db import models
from django.utils import timezone

class TokenVerification(models.Model):
    token = models.CharField(max_length=6, unique=True)
    expiration = models.DateTimeField()

    def is_valid(self):
        return timezone.now() < self.expiration
