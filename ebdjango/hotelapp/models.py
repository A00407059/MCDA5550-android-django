from django.db import models

# Create your models here.

class Hotel(models.Model):

    hotel_name = models.CharField(max_length=200, null=False)
    price = models.IntegerField()
    availability = models.BooleanField(null=True)

    def __str__(self):
        return self.hotel_name

class ReservationList(models.Model):

    hotel_name = models.CharField(max_length=200, null=False)
    checkin = models.CharField(max_length=200, null=False)
    checkout = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.hotel_name

class Guest(models.Model):
    guest_name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    reservation = models.ForeignKey(ReservationList, on_delete=models.CASCADE,
                                    related_name='guest_list')
