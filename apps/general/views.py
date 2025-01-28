from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..utils.models import IsAdminUser
from .models import PaymentMethod, University
from .serializers import PaymentMethodSerializer, UniversitySerializer


# List and Create View for PaymentMethod
class PaymentMethodListCreateView(ListCreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]

    # Additional filtering, searching, and sorting capabilities for PaymentMethod model
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'slug']
    search_fields = ['name']
    ordering_fields = ['pk', 'name']


# Retrieve, Update, and Delete View for PaymentMethod
class PaymentMethodDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]


# List and Create API View for University
class UniversityListCreateView(ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

    # Additional filtering, searching, and sorting capabilities for PaymentMethod model
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'slug']
    search_fields = ['name']
    ordering_fields = ['pk', 'name']


# Retrieve, Update, and Delete API View for University
class UniversityDetailView(RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]
