from django.shortcuts import render
from .models import Product

def home(req):
    products = Product.objects.all()
    return render(req, 'home.html', {'products': products})

def about(req):
    return render(req, 'about.html', {})