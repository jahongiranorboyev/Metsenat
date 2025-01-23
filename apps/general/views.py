
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import PaymentMethod, University
from .serializers import PaymentMethodSerializer, UniversitySerializer

# List and Create View for PaymentMethod
class PaymentMethodListCreateView(ListCreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated]

# Retrieve, Update, and Delete View for PaymentMethod
class PaymentMethodDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated]

# List and Create API View for University
class UniversityListCreateView(ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [IsAuthenticated]

# Retrieve, Update, and Delete API View for University
class UniversityDetailView(RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [IsAuthenticated]



