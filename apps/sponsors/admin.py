from django.contrib import admin
from .models import StudentSponsor


class StudentSponsorAdmin(admin.ModelAdmin):
    list_display = ('appeal', 'student', 'amount', 'created_at', 'updated_at')
    list_filter = ('student', 'appeal__status')
    search_fields = ('appeal__id', 'amount')
    raw_id_fields = ('appeal', 'student')
    ordering = ('-created_at',)



# Register the StudentSponsor model with the admin
admin.site.register(StudentSponsor, StudentSponsorAdmin)
