from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hotel, ReservationList
from .serializers import HotelSerializers, ReservationSerializers

def home(request):
    return HttpResponse('''
    <html>
    <body>
        <hi>Django RestAPI Assignment-Android<h1/>
        <ol>
            <li><a href="/read/">Hotel List</a></li>
            <li><a href="/create/">Hotel Reservation</a></Li>
        </ol>
        
    </body>
    </html>   
    
    ''')


@api_view(['GET', 'POST'])
def getListOfHotels(request):
    if request.method == 'GET':
        hotels_list = Hotel.objects.all()
        hotelSerializer = HotelSerializers(hotels_list, many=True)
        return Response(hotelSerializer.data)


@api_view(['GET', 'POST'])
def reservationConfirmation(request):
    if request.method == 'GET':
        reservation_list = ReservationList.objects.all()
        reservationSerializer = ReservationSerializers(reservation_list, many=True)
        return Response(reservationSerializer.data)

    if request.method == 'POST':

        reservation_request = request.data
        serialize_request_data = ReservationSerializers(data=reservation_request)

        if serialize_request_data.is_valid():
            serialize_request_data.save()

        return Response({"confirmation number": "OK"})

