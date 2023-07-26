from django.shortcuts import render
from .models import Brand, Staff
# Create your views here.

def home(request):
    brands = Brand.objects.all()
    return render(request, 'home.html', {'brands': brands})

def brand(request, brand_id):
    brand = Brand.objects.get(pk=brand_id)
    brand_models = brand.model_set.all()
    return render(request, 'brand.html', {'brand': brand, 'brand_models': brand_models})

def team(request):
    staff_members = Staff.objects.all()
    return render(request, 'team.html', {'staff_members': staff_members})
