from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import StudentSponsor
from .serializers import StudentSponsorSerializer

# List and Create View for StudentSponsor
class StudentSponsorListCreateView(generics.ListCreateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer
    permission_classes = [IsAuthenticated]

# Retrieve, Update, and Delete View for StudentSponsor
class StudentSponsorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer
    permission_classes = [IsAuthenticated]

