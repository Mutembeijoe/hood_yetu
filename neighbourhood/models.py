from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.



class Neighbourhood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    police_hotline= ArrayField(models.CharField(max_length=13, blank=True),size=2)
    hospital_hotline= ArrayField(models.CharField(max_length=13, blank=True),size=2)