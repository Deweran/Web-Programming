from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    flights = Flight.objects.all()
    context = {
        "flights": flights
    }
    return render(request, "flights/index.html", context)

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passenger.all()
    context = {
        "flight" : flight,
        "passengers": passengers,
        "non_passengers" : Passenger.objects.exclude(flights=flight).all()
    }
    return render(request, "flights/flight.html", context)

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(id = flight_id)
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flights:flight', args=(flight.id)))
