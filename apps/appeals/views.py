from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Appeal
from .permissions import AppealPermission
from .serializers import AppealSerializer
from apps.appeals.filters import AppealFilter

class AppealListCreateView(ListCreateAPIView):
    """
    API to list and create new appeals.
    Only accessible to `student` and `admin` for viewing appeals.
    Only admins can create new appeals.
    """
    queryset = Appeal.objects.order_by('-created_at')
    serializer_class = AppealSerializer
    filterset_class = AppealFilter
#    permission_classes = [AppealPermission]

    # Additional filtering, searching, and sorting capabilities for Appeal model



class AppealDetailView(RetrieveUpdateDestroyAPIView):
    """
    API for Retrieve, Update, and Delete (CRUD) operations on an appeal.
    Permissions vary by role:
    - Admin: Can perform all operations (view, update, delete).
    - Sponsor: Can update and delete their own appeals; can view all appeals.
    - Student: Can only view their own appeal; cannot update or delete.
    """
    queryset=Appeal.objects.order_by('-created_at')
    serializer_class=AppealSerializer
 #   permission_classes = [AppealPermission]

