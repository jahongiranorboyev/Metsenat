import json
import random

from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from apps.authentication.serializers import SendAuthCodeSerializer, AuthCodeConfirmSerializer

User = get_user_model()

class SendAuthCodeAPIView(CreateAPIView):
     serializer_class = SendAuthCodeSerializer


class AuthCodeConfirmApiView(CreateAPIView):
    serializer_class = AuthCodeConfirmSerializer

    def perform_create(self, serializer):
        pass


