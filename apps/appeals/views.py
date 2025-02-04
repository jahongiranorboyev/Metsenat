from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Appeal
from .permissions import AppealPermission
from .serializers import AppealSerializer



class AppealListCreateView(ListCreateAPIView):
    """
    API to list and create new appeals.
    Only accessible to `student` and `admin` for viewing appeals.
    Only admins can create new appeals.
    """
    queryset = Appeal.objects.order_by('-created_at')
    serializer_class = AppealSerializer
    permission_classes = [AppealPermission]

    # Additional filtering, searching, and sorting capabilities for Appeal model
    filterset_fields = ['status', 'payment_method', 'sponsor']
    search_fields = ['phone_number', 'amount']
    ordering_fields = ['pk', 'amount', 'available_balance', 'status']


class AppealDetailView(RetrieveUpdateDestroyAPIView):
    """
    API for Retrieve, Update, and Delete (CRUD) operations on an appeal.
    Permissions vary by role:
    - Admin: Can perform all operations (view, update, delete).
    - Sponsor: Can update and delete their own appeals; can view all appeals.
    - Student: Can only view their own appeal; cannot update or delete.
    """
    queryset = Appeal.objects.order_by('-created_at')
    serializer_class = AppealSerializer
    permission_classes = [AppealPermission]

    def get_object(self):
        """
        Check permissions based on the user's role when retrieving an appeal.
        """
        obj = super().get_object()

        return obj

    def update(self, request, *args, **kwargs):
        """
        Check permissions based on the user's role when updating appeal data.
        """
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Check permissions based on the user's role when deleting an appeal.
        """
        instance = self.get_object()

        return super().destroy(request, *args, **kwargs)
