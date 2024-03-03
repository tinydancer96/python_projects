from django.shortcuts import redirect, render

from .models import Flight

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
        "flight": flight
    })

def error(request):
    return render(request, "flights/error.html")
