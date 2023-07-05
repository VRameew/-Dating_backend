from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    # We use AbstractUser for creating users with non default struct

    avatar = models.ImageField(upload_to='avatars/')
    gender = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    longitude = models.FloatField()
    latitude = models.FloatField()


class Match(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='matches')
    liked_client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='liked_by')
    email_sent = models.BooleanField(default=False)