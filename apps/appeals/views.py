from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.exceptions import PermissionDenied

from .models import Appeal
from .serializers import AppealSerializer


# from ..users.models import UserModel


class AppealListCreateView(ListCreateAPIView):
    """
    API to list and create new appeals.
    Only accessible to `student` and `admin` for viewing appeals.
    Only admins can create new appeals.
    """
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    # permission_classes = [IsAuthenticated]

    # Additional filtering, searching, and sorting capabilities for Appeal model
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'payment_method', 'sponsor']
    search_fields = ['phone_number', 'amount']
    ordering_fields = ['pk', 'amount', 'available_balance', 'status']

    # def perform_create(self, serializer):
    #     """
    #     Only admins can create new appeals.
    #     """
    #     if self.request.user.role != UserModel.UserRole.SPONSOR :
    #         raise PermissionDenied("You must be an admin to create an appeal.")
    #     serializer.save()


class AppealDetailView(RetrieveUpdateDestroyAPIView):
    """
    API for Retrieve, Update, and Delete (CRUD) operations on an appeal.
    Permissions vary by role:
    - Admin: Can perform all operations (view, update, delete).
    - Sponsor: Can update and delete their own appeals; can view all appeals.
    - Student: Can only view their own appeal; cannot update or delete.
    """
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer

    # permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Check permissions based on the user's role when retrieving an appeal.
        """
        obj = super().get_object()

        # # Admin: Can view any appeal.
        # if self.request.user.role == UserModel.UserRole.ADMIN:
        #     return obj
        #
        # # Student: Can only view their own appeal.
        # if self.request.user.role == UserModel.UserRole.STUDENT:
        #     return obj
        #
        # # Sponsor: Can view, update, and delete their own appeal.
        # if self.request.user.role == UserModel.UserRole.SPONSOR:
        #     return obj

        # raise PermissionDenied("You do not have permission to access this appeal.")
        return obj

    def update(self, request, *args, **kwargs):
        """
        Check permissions based on the user's role when updating appeal data.
        """
        instance = self.get_object()

        # Admin: Can update any appeal.
        # if request.user.role == UserModel.UserRole.ADMIN:
        #     return super().update(request, *args, **kwargs)

        # Student: Cannot update any appeal.
        # raise PermissionDenied("Students cannot update any appeal.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Check permissions based on the user's role when deleting an appeal.
        """
        instance = self.get_object()

        # # Admin: Can delete any appeal.
        # if request.user.role == UserModel.UserRole.ADMIN:
        #     return super().destroy(request, *args, **kwargs)
        #
        # # Sponsor: Can only delete their own appeal.
        # if request.user.role == UserModel.UserRole.SPONSOR and instance.sponsor == request.user:
        #     return super().destroy(request, *args, **kwargs)

        # Student: Cannot delete any appeal.
        # raise PermissionDenied("Students cannot delete any appeal.")

        return super().destroy(request, *args, **kwargs)
