from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hotel
from .serializers import HotelSerializers

hotels = [
{'id':1, 'name':'Holiday INN', 'price':'100', 'available':True},
{'id':2, 'name':'Halifax Hotel', 'price':'120', 'available':True},
{'id':3, 'name':'Canada Hotel', 'price':'130', 'available':True},
{'id':4, 'name':'Marriet Hotel', 'price':'140', 'available':True}
]


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

def create(request):
    return HttpResponse("Create")

def read(request):
    return HttpResponse("Read!")


@api_view(['GET', 'POST'])
def getListOfHotels(request):
    if request.method == 'GET':

        hotelSerializer = HotelSerializers(hotels, many=True)

        return Response(hotelSerializer.data)


@api_view(['GET', 'POST'])
def Hotels_list(request):
    if request.method == 'GET':
        hotels_list = Hotel.objects.all()
        hotelSerializer = HotelSerializers(hotels_list, many=True)
        return Response(hotelSerializer.data)
