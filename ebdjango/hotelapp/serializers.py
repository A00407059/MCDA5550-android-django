from rest_framework import serializers
from .models import Hotel, ReservationList


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'price', 'available']


class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReservationList
        fields = ['hotel_name', 'checkin', 'checkout', 'guest_name', 'gender']
