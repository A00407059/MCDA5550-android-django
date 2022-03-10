from rest_framework import serializers
from .models import Hotel


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'price', 'available']
