from .models import AppUser
from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import timedelta


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']


class AppUserSerializers(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        fields=[
            
            'user',
            'first_name',
            'last_name',
            'phone',
            'email',

        ]



class RegisterSerializer(serializers.ModelSerializer):
    user=serializers.CharField(write_only=True)
    first_name=serializers.CharField(write_only=True)
    last_name=serializers.CharField(write_only=True)
    phone=serializers.CharField(write_only=True)
    email=serializers.EmailField(write_only=True)
