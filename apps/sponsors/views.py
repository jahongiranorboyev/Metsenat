from rest_framework import generics
from .models import StudentSponsor
from .serializers import StudentSponsorSerializer

# List and Create API View
class StudentSponsorListCreateView(generics.ListCreateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer

# Retrieve, Update, and Delete API View
class StudentSponsorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer
