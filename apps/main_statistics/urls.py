from django.urls import path
from .views import YearlyStatisticsAPIView

from django.urls import path
from .views import YearlyStatisticsAPIView

urlpatterns = [
    path('<int:year>/', YearlyStatisticsAPIView.as_view(), name='yearly-statistics'),
]