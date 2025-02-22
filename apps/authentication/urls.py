from django.urls import path
from .views import AuthCodeConfirmApiView, SendAuthCodeAPIView,LogoutView
urlpatterns = [
    path('send-verification-code/', SendAuthCodeAPIView.as_view(), name='send_verification_code'),
    path('login/', AuthCodeConfirmApiView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
