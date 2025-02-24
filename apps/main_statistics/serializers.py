from collections import defaultdict
from rest_framework import serializers
from apps.users.models import CustomUser
from apps.appeals.models import Appeal


# Serializer for Yearly Statistics
class YearlyStatisticsSerializer(serializers.Serializer):
    year = serializers.IntegerField()

    def to_representation(self, instance):
        year = instance.get("year")

        appeals = Appeal.objects.filter(created_at__year=year)
        students = CustomUser.objects.filter(role='student', created_at__year=year)

        # Data structure: {month: {day: {"student_count": ..., "appeal_count": ...} } }
        stats = defaultdict(lambda: defaultdict(lambda: {"student_count": 0, "appeal_count": 0}))
        monthly_totals = defaultdict(lambda: {"student_count": 0, "appeal_count": 0, "days": []})

        for student in students:
            month = student.created_at.month
            day = student.created_at.day
            stats[month][day]["student_count"] += 1
            monthly_totals[month]["student_count"] += 1

        for appeal in appeals:
            month = appeal.created_at.month
            day = appeal.created_at.day
            stats[month][day]["appeal_count"] += 1
            monthly_totals[month]["appeal_count"] += 1

        # Convert to desired format
        month_names = {
            1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
            7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
        }

        year_data = []
        for month, totals in monthly_totals.items():
            days_list = [
                {"day": str(day), "student_count": counts["student_count"], "appeal_count": counts["appeal_count"]}
                for day, counts in stats[month].items()
            ]
            year_data.append({
                "name": month_names[month],
                "student_count": totals["student_count"],
                "appeal_count": totals["appeal_count"],
                "month": days_list
            })

        return {str(year): year_data}
