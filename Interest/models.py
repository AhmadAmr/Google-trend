from django.db import models
from django.db.models.base import Model

class Historical(models.Model):
    date = models.DateTimeField()
    term = models.IntegerField()
    name = models.CharField(max_length=50)

class Region(models.Model):
    geoName=models.CharField(max_length=50)
    first_term = models.IntegerField()
    second_term= models.IntegerField()
    first_term_name=models.CharField(max_length=50)
    second_term_name=models.CharField(max_length=50)