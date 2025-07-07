from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.urls import path
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.models import Product
from django.contrib import messages

# Create your views here.

def home_views(request):
    username = 'none',
    if request.user.is_authenticated:
            username = request.user.username
    
    context = {
        'username' : username,
    }

    return render(request, 'home/home.html', context)


def login_views(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("../..")
        else:
            messages.error(request, 'usuario not exist')

    return render(request, "login/login.html")

def register_views(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username = username).exists():
            return render(request, 'login/register.html', {"erro" : "user exists"})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect('login')

    return render(request, "login/register.html")

def auth_views(request):
    if request.user.is_authenticated:
        return redirect('home')
    return HttpResponse("voce nao esta logado")

def logout_views(request):
    logout(request)
    return redirect('home')

def cart_views(request):
    if request.user.is_authenticated:
        return render(request, 'cart/cart.html')
    return HttpResponse("404")

def products_views(request):
    products = Product.objects.all()
    
    return render(request, 'products/products.html', {'products': products})


def addproductstocart_views(request):
    

    return redirect('cart')

def user_views(request):
    if request.user.is_authenticated:
        return render(request, 'login/user.html')
    else: 
        messages.error(request, 'You need to join.')
        return redirect('home')