from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    full_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    phone = models.CharField(max_length=15)
    address1 = models.CharField(max_length = 255)
    address2 = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 255, null=True, blank=True)
    zipcode = models.CharField(max_length = 255, null=True, blank=True)
    country = models.CharField(max_length = 255)
    
    class Meta:
        verbose_name_plural = "Shipping Area"
    def __str__(self):
        return f'Shippinh Address- {str(self.id)}'