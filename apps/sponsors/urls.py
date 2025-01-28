from django.urls import path
from .views import StudentSponsorListCreateView, StudentSponsorDetailView

urlpatterns = [
    path('', StudentSponsorListCreateView.as_view(), name='studentsponsor-list-create'),
    path('<uuid:pk>/', StudentSponsorDetailView.as_view(), name='studentsponsor-detail'),
]
