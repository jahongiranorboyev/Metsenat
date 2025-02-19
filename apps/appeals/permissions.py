from rest_framework.permissions import BasePermission, SAFE_METHODS
from apps.users.models import UserModel


class AppealPermission(BasePermission):
    """
    Custom permission for Appeal model:
    - Authenticated users can list (GET)
    - Only sponsors can create (POST)
    - Only sponsors and admins can retrieve, update, or delete
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        if request.method == "POST":
            return request.user.is_authenticated and request.user.role == UserModel.UserRole.SPONSOR

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # Ensure that the appeal is not approved before modifying
        if obj.status == Appeal.AppealStatus.Approved:
            return False

        # Only SPONSOR and ADMIN can modify
        return request.user.is_authenticated and request.user.role in [
            UserModel.UserRole.ADMIN,
            UserModel.UserRole.SPONSOR,
        ]
