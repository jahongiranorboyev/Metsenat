from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.permissions.serializers import UserPermissionListSerializer


class UserPermListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserPermissionListSerializer

    def get_queryset(self):
        user = self.request.user
        perms = user.get_all_permissions()
        print(perms)
        return perms
