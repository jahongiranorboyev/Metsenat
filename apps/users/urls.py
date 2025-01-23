from django.urls import path
from .views import StudentListCreateView, StudentDetailView, SponsorDetailView

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('sponsors/<int:pk>/', SponsorDetailView.as_view(), name='sponsor-detail'),
]
