from rest_framework import generics
from .models import StudentSponsor
from .serializers import StudentSponsorSerializer
from .permissions import StudentSponsorPermission


# List and Create View for StudentSponsor
class StudentSponsorListCreateView(generics.ListCreateAPIView):
    queryset = StudentSponsor.objects.order_by('-created_at')
    serializer_class = StudentSponsorSerializer
#    permission_classes = [StudentSponsorPermission]

    # Additional filtering, searching, and sorting capabilities for this model
    search_fields = ['appeal__sponsor_fullname', 'student__phone_number','amount']
    ordering_fields = ['amount']


# Retrieve, Update, and Delete View for StudentSponsor
class StudentSponsorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentSponsor.objects.order_by('-created_at')
    serializer_class = StudentSponsorSerializer
 #   permission_classes = [StudentSponsorPermission]
