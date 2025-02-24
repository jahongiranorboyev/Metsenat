from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TelegramAuthSerializer

from apps.authentication.serializers import SendAuthCodeSerializer, AuthCodeConfirmSerializer, LogoutSerializer


class SendAuthCodeAPIView(CreateAPIView):
     serializer_class = SendAuthCodeSerializer


class AuthCodeConfirmApiView(CreateAPIView):
    serializer_class = AuthCodeConfirmSerializer

    def perform_create(self, serializer):
        pass

class LogoutView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            refresh_token = serializer.validated_data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TelegramAuthView(APIView):
    def post(self, request):
        serializer = TelegramAuthSerializer(data=request.data)

        if serializer.is_valid():
            user_data = serializer.create_or_update_user(serializer.validated_data)
            return Response(user_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

