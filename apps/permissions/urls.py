from django.urls import path

from apps.permissions.views import UserPermListAPIView

urlpatterns = [
    path('me/',UserPermListAPIView.as_view(),name='user_perm_list'),
]