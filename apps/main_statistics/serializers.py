from rest_framework import serializers
from collections import defaultdict
from apps.users.models import CustomUser
from apps.appeals.models import Appeal


class YearlyStatisticsSerializer(serializers.Serializer):
    year = serializers.IntegerField()

    def to_representation(self, instance):
        year = instance.get("year")

        appeals = Appeal.objects.filter(created_at__year=year)
        students = CustomUser.objects.filter(role='student', created_at__year=year)

        # Nested dictionary: { oy: { kun: {"student_count": ..., "appeal_count": ...} } }
        stats = defaultdict(lambda: defaultdict(lambda: {"student_count": 0, "appeal_count": 0}))

        for student in students:
            month = student.created_at.month
            day = student.created_at.day
            stats[month][day]["student_count"] += 1

        for appeal in appeals:
            month = appeal.created_at.month
            day = appeal.created_at.day
            stats[month][day]["appeal_count"] += 1

        nested_stats = {str(month): {str(day): counts for day, counts in days.items()} for month, days in stats.items()}

        return {str(year): nested_stats}
