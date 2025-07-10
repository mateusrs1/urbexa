from django.contrib import admin

# Register your models here.
from .models import Product, Cart, CustomUser

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CustomUser)