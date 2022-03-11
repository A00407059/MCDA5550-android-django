from django.db import models

# Create your models here.

class Hotel(models.Model):

    name = models.CharField(max_length=200, null=False)
    price = models.IntegerField()
    available = models.BooleanField(null=True)

    def __str__(self):
        return self.name

class ReservationList(models.Model):

    hotel_name = models.CharField(max_length=200, null=False)
    checkin = models.CharField(max_length=200, null=False)
    checkout = models.CharField(max_length=200, null=False)
    guest_name = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.hotel_name