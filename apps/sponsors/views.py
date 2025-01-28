from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# from rest_framework.permissions import IsAuthenticated

from .models import StudentSponsor
from .serializers import StudentSponsorSerializer

# from ..utils.models import IsAdminUser


# List and Create View for StudentSponsor
class StudentSponsorListCreateView(generics.ListCreateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

    # Additional filtering, searching, and sorting capabilities for this model
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['phone_number', 'first_name', 'last_name']
    ordering_fields = ['pk', 'necessary_balance', 'available_balance']


# Retrieve, Update, and Delete View for StudentSponsor
class StudentSponsorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]
