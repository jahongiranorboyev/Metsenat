from django.urls import path
from .views import SendVerificationCodeAPIView, LoginAPIView

urlpatterns = [
    path('send-verification-code/', SendVerificationCodeAPIView.as_view(), name='send_verification_code'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
