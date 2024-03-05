from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", {
            "message": f"Flight {flight_id} does not exist",
        })
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def error(request):
    return render(request, "flights/error.html")

def book(request, flight_id):
    try:
        if request.method == "POST":
            flight = Flight.objects.get(pk=flight_id)
            passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
            passenger.flights.add(flight)
            return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
        else:
            return render(request, "flights/error.html", {
            "message": f"Flight ID {flight_id} does not exist. Please book another flight"
        })
    except:
        return render(request, "flights/error.html", {
            "message": f"Flight ID {flight_id} does not exist. Please book another flight"
        })
