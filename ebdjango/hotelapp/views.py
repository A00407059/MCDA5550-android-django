from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hotel
from .serializers import HotelSerializers


def home(request):
    return HttpResponse("Hello Jongwon Shinn")

def create(request):
    return HttpResponse("Create")

def read(request):
    return HttpResponse("Read!")


@api_view(['GET', 'POST'])
def getListOfHotels(request):
    if request.method == 'GET':
        hotels_list = Hotel.objects.all()
        hotelSerializer = HotelSerializers(hotels_list, many=True)

        return Response(hotelSerializer.data)
