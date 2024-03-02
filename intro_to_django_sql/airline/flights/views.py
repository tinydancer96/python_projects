from django.shortcuts import redirect, render

from .models import Flight

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })
