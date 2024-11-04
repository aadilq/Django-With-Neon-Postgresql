from django.db import models

# Create your models here.

class Element(models.Model):
    name = models.TextField()
    symbol = models.CharField(max_length=3)
    atomic_number = models.IntegerField()
