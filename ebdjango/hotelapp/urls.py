from django.urls import path
from . import views

urlpatterns=[

    path('', views.home, name="home"),
    path("hotel_list/", views.getListOfHotels, name="hotelList"),
    path('create/', views.create),
    path('read/', views.read)
]