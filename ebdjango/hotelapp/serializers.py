from rest_framework import serializers
from .models import Hotel, ReservationList, Guest


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'price', 'availability']

class GuestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['guest_name', 'gender']


class ReservationSerializers(serializers.ModelSerializer):
    guest_list = GuestSerializers(many=True)

    class Meta:
        model = ReservationList
        fields = ['hotel_name', 'checkin', 'checkout', 'guest_list']


