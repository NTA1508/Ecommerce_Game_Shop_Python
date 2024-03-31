from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm

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

def register_user(req):
    form = SignUpForm()
    if req.method == "POST":
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(req, user)
            messages.success(req, "You have successfully registered!")
            return redirect('home')
    
    return render(req, "register.html", {'form': form})

def product(req, pk):
    product = Product.objects.get(id = pk)
    return render(req, 'product.html', {'product': product})

def category(req, foo):
    foo = foo.replace('?', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(req, 'category.html', {'products': products, 'category': category})
    except Category.DoesNotExist:
        messages.error(req, "That category doesn't exist.")
        return redirect('home')

def update_user(req):
    if req.user.is_authenticated:
        current_user = User.objects.get(id=req.user.id)
        user_form = UpdateUserForm(req.POST or None, instance = current_user)
        if user_form.is_valid():
            user_form.save()
            
            login(req, current_user)
            messages.success(req, "User has been updated!")
            return redirect('home')
        return render(req, "update_user.html", {'user_form': user_form})
    else:
        messages.error(req, "Please Login!")
        return redirect('home')
    
def update_password(req):
    if req.user.is_authenticated:
        current_user = req.user
        if req.method == 'POST':
            form = ChangePasswordForm(current_user, req.POST)
            if form.is_valid():
                form.save()
                messages.success(req, "Your password has been change!")
                login(req, current_user)
                return redirect('home')
            else:
                for error in list(form.errors.values()):
                    messages.error(req, error)
                    return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(req, "update_password.html", {'form': form})
    else:
        messages.error(req, "Please Login!")
        return redirect('home')