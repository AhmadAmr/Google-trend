from django.db import models

class Historical(models.Model):
    date = models.DateTimeField()
    term = models.IntegerField()
    name = models.CharField(max_length=50)
