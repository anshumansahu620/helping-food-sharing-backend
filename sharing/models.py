from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

import uuid


class AppUser(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(unique=True)
    email=models.EmailField(unique=True)
    




    
class   HelpRequest(models.Model):
    request_by=models.ForeignKey(AppUser,on_delete=models.CASCADE)
    address=models.CharField(max_length=2000)
    pin_code=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text="Latitude in decimal degrees"
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text="Longitude in decimal degrees"
    )

    accuracy_meters = models.FloatField(null=True, blank=True)
    altitude_meters = models.FloatField(null=True, blank=True)
    

    created_at = models.DateTimeField(auto_now_add=True)






    

    








