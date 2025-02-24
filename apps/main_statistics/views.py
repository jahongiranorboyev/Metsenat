from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .serializers import YearlyStatisticsSerializer


class YearlyStatisticsAPIView(RetrieveAPIView):
    serializer_class = YearlyStatisticsSerializer
    lookup_url_kwarg = "year"

    def get_object(self):
        year = self.kwargs.get("year")
        try:
            year_int = int(year)
        except (ValueError, TypeError):
            return Response({"error": "Invalid year format"}, status=400)
        return {"year": year_int}

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)