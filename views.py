
from django.shortcuts import render, get_object_or_404
from .models import Car

def home(request):
    cars = Car.objects.all()
    return render(request, "cars/index.html", {"cars": cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, "cars/detail.html", {"car": car})
