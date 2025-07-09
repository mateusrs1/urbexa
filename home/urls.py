
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_views, name="home"),
    path('login/', views.login_views, name="login"),
    path('register/', views.register_views, name="register"),
    path('auth/', views.auth_views, name='auth'),
    path('cart/', views.cart_views, name='cart'),
    path('cart/add/<int:cart_id>/', views.cartadd_views, name='add_cart'),
    path('cart/rem/<int:cart_id>/', views.cartrem_views, name='rem_cart'),
    path('products/', views.products_views, name="products"),
    path('products/addtocart/<int:product_id>/', views.addproductstocart_views, name="addtocart"),
    path('auth/logout', views.logout_views, name="logout"),
    path('auth/user', views.user_views, name="user"),
    path('auth/user/edit', views.edituser_view, name="edit")
]
