from .models import AppUser,HelpRequest
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
        model=AppUser
        fields=[
            
            'user',
            'first_name',
            'last_name',
            'phone',
            'email',

        ]



class RegisterSerializer(serializers.ModelSerializer):
    
    phone=serializers.CharField(write_only=True)
    
    class Meta:
        model=User
        fields=[
            "username","email","password","first_name","last_name","phone"
        ]
        extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data):
        
        phone = validated_data.pop("phone")

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        
       
        AppUser.objects.create(
            user=user,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone=phone,      
        )
        return user
    

class HelpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpRequest
        fields = (
            'request_by',
            'address',
            'pin_code',
            'country',
            'latitude',
            'longitude',
            'accuracy_meters',
            'altitude_meters',
            'created_at',
        )
        read_only_fields = ('request_by', 'created_at')


   
       
     