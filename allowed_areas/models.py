# Create your models here.
from django.contrib.gis.db import models

class Allowed_areas(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)