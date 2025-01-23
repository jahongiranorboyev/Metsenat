from rest_framework import generics
from .models import Appeal
from .serializers import AppealSerializer

# List and Create API View
class AppealListCreateView(generics.ListCreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer

# Retrieve, Update, and Delete API View
class AppealDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
