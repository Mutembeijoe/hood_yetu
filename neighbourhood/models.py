from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Business(models.Model):
    FOOD = 1
    BEAUTY = 2
    SOCIAL = 3
    ENTERTAINMENT = 4
    HOUSING = 5

    BUSINESS_CATEGORIES = [
        (FOOD, 'Food and Beverages'),
        (BEAUTY, 'Beauty shops'),
        (SOCIAL,'Social Amentity'),
        (ENTERTAINMENT, 'Entertainment'),
        (HOUSING, 'Housing'),
    ]

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    category = models.PositiveSmallIntegerField(choices=BUSINESS_CATEGORIES)


class Neighbourhood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    police_hotline= ArrayField(models.CharField(max_length=13, blank=True),size=3, blank=True, null=True)
    hospital_hotline= ArrayField(models.CharField(max_length=13, blank=True),size=3, blank=True, null=True)

