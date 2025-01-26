from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == get_user_model().UserRole.ADMIN