from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .permissions import IsAdminUser
from .models import PaymentMethod, University
from .serializers import PaymentMethodSerializer, UniversitySerializer


# List and Create View for PaymentMethod
class PaymentMethodListCreateView(ListCreateAPIView):
    queryset = PaymentMethod.objects.order_by('-created_at')
    serializer_class = PaymentMethodSerializer
#    permission_classes = [IsAdminUser]

    # Additional filtering, searching, and sorting capabilities for PaymentMethod model
    filterset_fields = ('name', )
    search_fields = ('name',)
    ordering_fields = ('name',)


# Retrieve, Update, and Delete View for PaymentMethod
class PaymentMethodDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PaymentMethod.objects.order_by('-created_at')
    serializer_class = PaymentMethodSerializer
 #   permission_classes = [IsAdminUser]


# List and Create API View for University
class UniversityListCreateView(ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
  #  permission_classes = [IsAdminUser]

    # Additional filtering, searching, and sorting capabilities for PaymentMethod model
    filterset_fields = ('name', )
    search_fields = ('name',)
    ordering_fields = ('name',)


# Retrieve, Update, and Delete API View for University
class UniversityDetailView(RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
   # permission_classes = [IsAdminUser]
