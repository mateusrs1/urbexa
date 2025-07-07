
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_views, name="home"),
    path('login/', views.login_views, name="login"),
    path('register/', views.register_views, name="register"),
    path('auth/', views.auth_views, name='auth'),
    path('cart/', views.cart_views, name='cart'),
    path('products/', views.products_views, name="products"),
    path('products/addtocart', views.addproductstocart_views, name="addtocart"),
    path('auth/logout', views.logout_views, name="logout"),
    path('auth/user', views.user_views, name="user")
]
