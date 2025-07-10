from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
# Create your models here.

class CustomUser(AbstractUser):
    img = models.ImageField(upload_to='users/', null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    phone = PhoneNumberField(region='BR', null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="Product/")

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quant = models.PositiveIntegerField(default=1)
    unitval = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    totalvalue = models.DecimalField(max_digits=10, decimal_places=2, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.unitval = self.product_id.price
        self.totalvalue = self.unitval * self.quant
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_id.name} x {self.quant}"

#class User_home(models.Model):
#    name = models.CharField(max_length=100)
#    email = models.EmailField(unique=True)
#    password = models.CharField(max_length=30)
#    end = models.CharField(max_length=255)
#    image = models.ImageField(upload_to="perfil/")

#    def __str__(self):
#        return self.name