from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.urls import path
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.models import Product, Cart, CustomUser
from django.contrib import messages

# Create your views here.

def home_views(request):
    products = Product.objects.all()
    username = 'none'
    img = '/static/images/user-perfil.png'
    if request.user.is_authenticated:
            username = request.user.username
            if hasattr(request.user, 'img') and request.user.img:
                img = request.user.img.url
    context = {
        'username' : username,
        'img' : img,
        'products' : products
    }

    return render(request, 'home/home.html', context)


def login_views(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'usuario not exist')

    return render(request, "login/login.html")

def register_views(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        city = request.POST['city']
        state = request.POST['state']
        address = request.POST['address']
        phone = request.POST['phone']
        img = request.FILES.get('img')

        if CustomUser.objects.filter(username = username).exists():
            return render(request, 'login/register.html', {"erro" : "user exists"})
        
        user = CustomUser.objects.create_user(username=username, email=email, password=password, phone=phone, address=address, city=city, state=state, img=img)
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
        products = Cart.objects.filter(user_id=request.user)
        total_cart_value = sum(item.totalvalue for item in products)
        context= {
            'products' : products,
            'total' : total_cart_value
        }
        return render(request, 'cart/cart.html', context)
    else:
        messages.error(request, 'You need to join.')
        return redirect('home')

def cartadd_views(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id, user_id=request.user)
    item.quant += 1
    item.save()
    return redirect('cart')

def cartrem_views(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id, user_id=request.user)
    if item.quant > 1:
        item.quant -= 1
        item.save()
    else:
        item.delete() 
    return redirect('cart')

def cartfinish_views(request):
    messages.error(request, 'You need to pay, but the site ends here')
    return redirect('home')

def products_views(request):
    products = Product.objects.all()
    
    return render(request, 'products/products.html', {'products': products})


def addproductstocart_views(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = Cart.objects.get_or_create(
            user_id=request.user,
            product_id=product,
            defaults={
                'quant': 1,
                'unitval': product.price,
                'totalvalue': product.price
            }
        )
        if not created:
            cart_item.quant += 1
            cart_item.save()
        messages.error(request, 'product added to cart!')
        return redirect('products')
        
    else:
        return redirect('login')

def user_views(request):
    
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email
        address = request.user.address
        state = request.user.state
        city = request.user.city
        phone = request.user.phone
        img = request.user.img.url if request.user.img and request.user.img.name else '/static/images/user-perfil.png'

        context = {
        'username' : username,
        'email' : email,
        'address' : address,
        'state' : state,
        'city' : city,
        'phone' :phone,
        'img' : img
        }

        return render(request, 'login/user.html',context)
    else: 
        messages.error(request, 'You need to join.')
        return redirect('home')
    
def edituser_view(request):
    user = request.user

    if request.method == 'POST':
        user.city = request.POST.get('city')
        user.state = request.POST.get('state')
        user.address = request.POST.get('address')
        user.phone = request.POST.get('phone')

        if 'img' in request.FILES and request.FILES['img']:
            user.img = request.FILES['img']

        user.save()
        messages.success(request, 'Informações atualizadas com sucesso!')
        return redirect('user')  # redireciona para a view de perfil

    context = {
        'username': user.username,
        'email': user.email,
        'address': user.address,
        'state': user.state,
        'city': user.city,
        'phone': user.phone,
        'img': user.img.url if user.img and hasattr(user.img, 'url') else '/static/images/user-perfil.png',
    }

    return render(request, 'login/edit.html', context)
    
def edituserimg_view(request):
    
    return redirect("user")