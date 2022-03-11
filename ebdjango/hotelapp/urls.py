from django.urls import path
from . import views

urlpatterns=[

    path('', views.home, name="home"),
    path('create/', views.reservationConfirmation, name="reservationlist"),
    path('read/', views.getListOfHotels, name="hotelList")
]