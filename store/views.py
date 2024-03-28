from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(req):
    products = Product.objects.all()
    return render(req, 'home.html', {'products': products})

def about(req):
    return render(req, 'about.html', {})

def login_user(req):
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            messages.success(req, "Login successful!!!")
            return redirect('home')
        else:
            messages.error(req, "Login failed. Please check your credentials.")
            return redirect('login')
    else:
        return render(req, 'login.html', {})

def logout_user(req):
    logout(req)
    messages.success(req, ("You have been logged out..."))
    return redirect('home')