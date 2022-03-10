from django.urls import path
from . import views

urlpatterns=[

    path("home/", views.home, name="home"),
    path("hotel_list/", views.getListOfHotels, name="hotelList")

]