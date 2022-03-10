from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=200, null=False)
    price = models.IntegerField()
    available = models.BooleanField(null=True)

