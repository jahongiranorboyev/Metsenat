from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Appeal
from .serializers import AppealSerializer

# List and Create View for Appeal
class AppealListCreateView(generics.ListCreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    permission_classes = [IsAuthenticated]

# Retrieve, Update, and Delete View for Appeal
class AppealDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    permission_classes = [IsAuthenticated]

