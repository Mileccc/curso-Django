# pylint: disable=no-member
from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant
# Create your views here.


def create(request):
    place = Place(name="Lugar1", address="Calle Demo")
    place.save()

    restaurant = Restaurant(place=place, number_of_employees=5)
    restaurant.save()

    return HttpResponse(restaurant.place.name)
