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

class SendVerificationCodeAPIView(APIView):
    def post(self, request):
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            phone_number = data.get("phone_number")

        except json.JSONDecodeError:
            # Handle invalid JSON format
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        # Ensure the phone number is provided
        if not phone_number:
            return JsonResponse({"error": "Phone number is required"}, status=400)

        # Generate a random 4-digit verification code
        verification_code = random.randint(1000, 9999)

        # Simulate sending the verification code (e.g., via SMS)
        print(f"Verification code sent to {phone_number}: {verification_code}")

        # Store the verification code and phone number in the session
        request.session['verification_code'] = str(verification_code)
        request.session['phone_number'] = phone_number

        # Return a success response
        return JsonResponse({
            "message": "Verification code sent",
            "phone_number": phone_number,
            "verification_code": verification_code
        })

class LoginAPIView(APIView):
    def post(self, request):
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            phone_number = data.get("phone_number")
            verification_code = data.get("verification_code")
        except json.JSONDecodeError:
            # Handle invalid JSON format
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        # Ensure both phone number and verification code are provided
        if not phone_number or not verification_code:
            return JsonResponse({"error": "Phone number and verification code are required"}, status=400)

        # Retrieve the stored verification code and phone number from the session
        stored_code = request.session.get('verification_code')
        stored_phone = request.session.get('phone_number')

        # Check if verification data exists or if the session has expired
        if not stored_code or not stored_phone:
            return JsonResponse({"error": "No verification code sent or session expired"}, status=400)

        # Validate the phone number and verification code
        if phone_number != stored_phone or verification_code != stored_code:
            return JsonResponse({"error": "Invalid phone number or verification code"}, status=400)

        # Retrieve or create a user based on the phone number
        user, created = User.objects.get_or_create(phone_number=phone_number)

        if created:
            # Set an unusable password for new users
            user.set_unusable_password()
            user.save()

        # Generate JWT tokens for the user
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Clear the session data for security
        del request.session['verification_code']
        del request.session['phone_number']

        return JsonResponse({
            "message": "Login successful",
            "access_token": access_token,
            "refresh_token": refresh_token
        })
