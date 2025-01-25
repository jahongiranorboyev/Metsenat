from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random

User = get_user_model()


@csrf_exempt
def send_verification_code(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        if not phone_number:
            return JsonResponse({"error": "Phone number is required"}, status=400)

        verification_code = random.randint(1000, 9999)
        # Simulating SMS sending here
        print(f"Verification code sent to {phone_number}: {verification_code}")
        request.session['verification_code'] = str(verification_code)
        request.session['phone_number'] = phone_number
        return JsonResponse(
            {"message": "Verification code sent",
             "verfication_code": verification_code,
             "phone_number": phone_number
             }
        )
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def login(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")

        if not phone_number or not password:
            return JsonResponse({"error": "Phone number and password are required"}, status=400)

        try:
            user = User.objects.get(phone_number=phone_number)
            if user.check_password(password):
                return JsonResponse({"message": "Login successful"})
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
