from django.db import models
from django.contrib.auth.models import AbstractUser
from neighbourhood.models import Neighbourhood

# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', default='default.jpg')
    bio = models.TextField(blank=True, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='residents', default=1, on_delete=models.SET_DEFAULT)



