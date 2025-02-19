from rest_framework import serializers
from .models import StudentSponsor
from apps.utils.serializers import  BaseModelSerializer


class StudentSponsorSerializer(BaseModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = '__all__'
