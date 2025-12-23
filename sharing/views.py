
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import AppUser,HelpRequest
from rest_framework.serializers import Serializer
from rest_framework.authentication import TokenAuthentication
from .serializers import RegisterSerializer,HelpRequestSerializer

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HelpRequestView(generics.CreateAPIView):
    queryset = HelpRequest.objects.all()
    serializer_class = HelpRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            app_user = AppUser.objects.get(user=self.request.user)
        except AppUser.DoesNotExist:
            raise serializers.ValidationError(
                {'error': 'User does not exist. Please login.'}
            )

        serializer.save(request_by=app_user)



