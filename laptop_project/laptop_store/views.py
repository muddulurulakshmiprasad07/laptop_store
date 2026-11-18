from django.shortcuts import render
from .models import Laptop

def laptop_home(request):
    laptops = Laptop.objects.all()

    return render(request, 'index.html', {
        'laptops': laptops
    })