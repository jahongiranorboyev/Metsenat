from rest_framework import generics
from .models import CustomUser
from .serializers import StudentSerializer
from .serializers import SponsorSerializer
from rest_framework.permissions import IsAuthenticated

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(user_type='student')
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

# Retrieve, Update, and Delete View for a Student
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(user_type='student')
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]



# List and Create View for Sponsor
class SponsorListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(user_type='sponsor')
    serializer_class = SponsorSerializer
    permission_classes = [IsAuthenticated]  # Login talab qilinadi

# Retrieve, Update, and Delete View for a Sponsor
class SponsorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(user_type='sponsor')
    serializer_class = SponsorSerializer
    permission_classes = [IsAuthenticated]



