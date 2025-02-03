from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.users.models import CustomUser


class UserPermission(BasePermission):
    """
    Custom permission for the CustomUser model:
    - List (GET) → Only authenticated users.
    - Retrieve (GET /id/) → Admins can view any user. Sponsors can view their own profile and students. Students can view themselves and sponsors.
    - Create (POST) → Only admins can create users.
    - Update (PUT/PATCH) → Admins can update any user. Sponsors can update only their own profile. Students cannot update anyone.
    - Delete (DELETE) → Admins can delete any user. Sponsors can delete only their own profile. Students cannot delete anyone.
    """

    def has_permission(self, request, view):
        # List view: Only authenticated users can access
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        # Create: Only admins can create users
        if request.method == "POST":
            return request.user.is_authenticated and request.user.role == CustomUser.UserRole.ADMIN

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Retrieve:
        if request.method in SAFE_METHODS:
            if request.user.role == CustomUser.UserRole.ADMIN:
                return True
            if request.user.role == CustomUser.UserRole.STUDENT:
                return obj == request.user or obj.role == CustomUser.UserRole.SPONSOR
            if request.user.role == CustomUser.UserRole.SPONSOR:
                return obj == request.user or obj.role == CustomUser.UserRole.STUDENT

        # Update:
        if request.method in ["PUT", "PATCH"]:
            if request.user.role == CustomUser.UserRole.ADMIN:
                return True
            if request.user.role == CustomUser.UserRole.SPONSOR:
                return obj == request.user

        # Delete:
        if request.method == "DELETE":
            if request.user.role == CustomUser.UserRole.ADMIN:
                return True
            if request.user.role == CustomUser.UserRole.SPONSOR:
                return obj == request.user
        return False
