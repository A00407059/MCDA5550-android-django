from django.urls import path
from . import views

urlpatterns=[

    path('', views.home, name="home"),
    path("hotel_list/", views.Hotels_list, name="hotelList2"),
    path('create/', views.reservationConfirmation, name="reservationlist"),
    path('read/', views.getListOfHotels, name="hotelList")
]