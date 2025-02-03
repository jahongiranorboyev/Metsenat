from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.users.models import UserModel


class StudentSponsorPermission(BasePermission):
    """
    Custom permission for the StudentSponsor model:
    - List (GET) and Retrieve (GET /id/) → Only authenticated users can view.
    - Create (POST), Update (PUT/PATCH), Delete (DELETE) → Only admins can perform these actions.
    """

    def has_permission(self, request, view):
        # Allow authenticated users to view the list or retrieve a specific object
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        # Only admins can create, update, or delete
        return request.user.is_authenticated and request.user.role == UserModel.UserRole.ADMIN

    def has_object_permission(self, request, view, obj):
        # Allow authenticated users to retrieve objects
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        # Only admins can modify or delete
        return request.user.role == UserModel.UserRole.ADMIN
