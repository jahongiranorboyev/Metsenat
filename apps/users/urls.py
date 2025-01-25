from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    # Endpoint for listing and creating users
    path('', UserListCreateAPIView.as_view(), name='user-list-create'),

    # Endpoint for retrieving, updating, and deleting a specific user
    path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
]

