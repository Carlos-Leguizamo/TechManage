from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token_verification = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username
