from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import CustomUser
from .permissions import UserPermission
from .serializers import CustomUserSerializer

class UserListCreateAPIView(ListCreateAPIView):
    """
    API to view the list of users and create new users.
    Only accessible to authenticated users for listing.
    Only admins can create new users.
    """
    queryset = CustomUser.objects.order_by('-created_at')
    serializer_class = CustomUserSerializer
#    permission_classes = [UserPermission]

    # Filtering, searching, and sorting capabilities
    filterset_fields = ['role', 'degree', 'university','sponsor_type']
    search_fields = ['phone_number', 'first_name', 'last_name']
    ordering_fields = ['necessary_balance', 'available_balance']


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    API for Retrieve, Update, and Delete (CRUD) operations on a user.
    Permissions vary by role:
    - Admin: Can perform all operations.
    - Sponsor: Can view, update, and delete their own profile; can only view students.
    - Student: Can view their own profile or sponsors; cannot update or delete.
    """
    queryset = CustomUser.objects.order_by('-created_at')
    serializer_class = CustomUserSerializer
 #   permission_classes = [UserPermission]
