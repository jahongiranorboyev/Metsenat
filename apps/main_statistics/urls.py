from django.urls import path
from .views import YearlyStatisticsAPIView

urlpatterns = [
    path('<str:year>/', YearlyStatisticsAPIView.as_view(), name='yearly-statistics'),
]