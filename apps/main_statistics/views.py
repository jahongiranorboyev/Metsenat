from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .serializers import YearlyStatisticsSerializer

class YearlyStatisticsAPIView(RetrieveAPIView):
    serializer_class = YearlyStatisticsSerializer

    def retrieve(self, request, *args, **kwargs):
        year = self.kwargs.get("year")
        try:
            year_int = int(year)
        except (ValueError, TypeError):
            return Response({"error": "Invalid year format"}, status=400)
        serializer = self.get_serializer({"year": year_int})
        return Response(serializer.data)
