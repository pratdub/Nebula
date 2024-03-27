from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
from UserAuth import settings


class User(AbstractUser) :
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(unique = True)
    email_verified = models.BooleanField(default = False)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) :
        return self.username
    

class OTP(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'otp')
    otp = models.CharField(max_length = 4)
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self) :
        return f"{self.user.username} - {self.otp}"

    def save(self, *args, **kwargs) :
        # Delete OTPs older than 5 minutes
        ten_minutes_ago = timezone.now() - timedelta(minutes = 5)
        OTP.objects.filter(created_at__lt = ten_minutes_ago).delete()
        super().save(*args, **kwargs)
