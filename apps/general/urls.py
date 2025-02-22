from django.urls import path
from .views import PaymentMethodListCreateView, PaymentMethodDetailView
from .views import UniversityListCreateView, UniversityDetailView

urlpatterns = [
    path('universities/', UniversityListCreateView.as_view(), name='university-list-create'),
    path('universities/<uuid:pk>/', UniversityDetailView.as_view(), name='university-detail'),
    path('payment-methods/', PaymentMethodListCreateView.as_view(), name='paymentmethod-list-create'),
    path('payment-methods/<uuid:pk>/', PaymentMethodDetailView.as_view(), name='paymentmethod-detail'),
]
