from django.contrib import admin
from django.template.response import TemplateResponse
from datetime import date
from collections import defaultdict

from apps.users.models import CustomUser
from apps.appeals.models import Appeal
from .models import DailyStatistics

class DummyQuerySet:
    def __iter__(self):
        return iter([])
    def count(self):
        return 0
    def __len__(self):
        return 0

@admin.register(DailyStatistics)
class DailyStatisticsAdmin(admin.ModelAdmin):
    change_list_template = "admin/dailystatistics_changelist.html"

    def get_queryset(self, request):
        return DummyQuerySet()

    def changelist_view(self, request, extra_context=None):
        year_param = request.GET.get('year')
        try:
            year = int(year_param) if year_param else date.today().year
        except ValueError:
            year = date.today().year

        stats = defaultdict(lambda: defaultdict(lambda: {"student_count": 0, "appeal_count": 0}))

        students = CustomUser.objects.filter(role='student', created_at__year=year)
        appeals = Appeal.objects.filter(created_at__year=year)

        for student in students:
            month = student.created_at.month
            day = student.created_at.day
            stats[month][day]["student_count"] += 1

        for appeal in appeals:
            month = appeal.created_at.month
            day = appeal.created_at.day
            stats[month][day]["appeal_count"] += 1

        context = {
            **self.admin_site.each_context(request),
            "title": f"Statistics for Year: {year}",
            "stats": dict(stats),
            "year": year,
            "app_label": "main_statistics",
        }
        return TemplateResponse(request, self.change_list_template, context)
