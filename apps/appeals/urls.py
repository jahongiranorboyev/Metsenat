from django.urls import path
from .views import AppealListCreateView, AppealDetailView

urlpatterns = [
    path('', AppealListCreateView.as_view(), name='appeal-list-create'),
    path('<uuid:pk>/', AppealDetailView.as_view(), name='appeal-detail'),
]
