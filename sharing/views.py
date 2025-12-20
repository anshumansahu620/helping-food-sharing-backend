from django.shortcuts import render
from rest_framework import generics, permissions,status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .serializers import RegisterSerializer

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


    