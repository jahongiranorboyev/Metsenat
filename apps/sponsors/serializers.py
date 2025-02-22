from rest_framework import serializers
from .models import StudentSponsor
from apps.utils.serializers import BaseModelSerializer


class StudentSponsorSerializer(BaseModelSerializer):
    student = serializers.SerializerMethodField()
    appeal = serializers.SerializerMethodField()

    class Meta:
        model = StudentSponsor
        fields = ['id','student', 'appeal', 'amount']

    def get_student(self, obj):
        """
        returns students' names
        """
        return obj.student.full_name if obj.student else ''

    def get_appeal(self, obj):
        """
        returns appeals' names
        """
        return obj.appeal.sponsor_fullname if obj.appeal else ''
