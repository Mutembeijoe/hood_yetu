from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', default='default.jpg')
    bio = models.TextField(blank=True, null=True)



