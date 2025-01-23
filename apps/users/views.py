from rest_framework import generics
from .models import CustomUser
from .serializers import StudentSerializer
from .serializers import SponsorSerializer

# List and Create View for Students
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(user_type='student')
    serializer_class = StudentSerializer

# Retrieve, Update, and Delete View for a Student
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(user_type='student')
    serializer_class = StudentSerializer



# Retrieve, Update, and Delete View for a Sponsor
class SponsorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(user_type='sponsor')
    serializer_class = SponsorSerializer

