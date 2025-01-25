from django.template.context_processors import request
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import CustomUser, UserModel
from .serializers import CustomUserSerializer

class UserListCreateAPIView(ListCreateAPIView):
    """
    API to view the list of users and create new users.
    Only accessible to roles `student` and `admin` for CRUD operations.
    """
    queryset = CustomUser.objects.filter(role__in=[UserModel.UserRole.STUDENT, UserModel.UserRole.SPONSOR])
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    # Filtering, searching, and sorting capabilities
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['role', 'degree', 'university']
    search_fields = ['phone_number', 'first_name', 'last_name']
    ordering_fields = ['pk', 'balance', 'available_balance']

    def perform_create(self, serializer):
        """
        Additional checks when creating a user.
        Only admins are allowed to create new users.
        """
        if self.request.user.role != CustomUser.UserRole.ADMIN:
            raise PermissionDenied("You must be an admin to create a user.")
        serializer.save()


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    API for Retrieve, Update, and Delete (CRUD) operations on a user.
    Permissions vary by role:
    - Admin: Can perform all operations.
    - Sponsor: Can view, update, and delete their own profile; can only view students.
    - Student: Can view their own profile or sponsors; cannot update or delete.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Check permissions based on the user's role when retrieving user data.
        """
        obj = super().get_object()

        # Admin: Can view any user.
        if self.request.user.role == CustomUser.UserRole.ADMIN:
            return obj

        # Student: Can only view their own profile or sponsors.
        if self.request.user.role == CustomUser.UserRole.STUDENT:
            if obj == self.request.user or obj.role == CustomUser.UserRole.SPONSOR:
                return obj
            raise PermissionDenied("Students can only view themselves or sponsors.")

        # Sponsor: Can only view their own profile or students.
        if self.request.user.role == CustomUser.UserRole.SPONSOR:
            if obj == self.request.user or obj.role == CustomUser.UserRole.STUDENT:
                return obj
            raise PermissionDenied("Sponsors can only view themselves or students.")

        # Deny access if no conditions are met.
        raise PermissionDenied("You do not have permission to access this user's data.")

    def update(self, request, *args, **kwargs):
        """
        Check permissions based on the user's role when updating user data.
        """
        instance = self.get_object()

        # Admin: Can update any user.
        if request.user.role == CustomUser.UserRole.ADMIN:
            return super().update(request, *args, **kwargs)

        # Sponsor: Can only update their own profile.
        if request.user.role == CustomUser.UserRole.SPONSOR and instance == request.user:
            return super().update(request, *args, **kwargs)

        # Student: Cannot update their own profile or others.
        raise PermissionDenied("Students cannot update any user.")

    def destroy(self, request, *args, **kwargs):
        """
        Check permissions based on the user's role when deleting a user.
        """
        instance = self.get_object()

        # Admin: Can delete any user.
        if request.user.role == CustomUser.UserRole.ADMIN:
            return super().destroy(request, *args, **kwargs)

        # Sponsor: Can only delete their own profile.
        if request.user.role == CustomUser.UserRole.SPONSOR and instance == request.user:
            return super().destroy(request, *args, **kwargs)

        # Student: Cannot delete any user.
        raise PermissionDenied("Students cannot delete any user.")
