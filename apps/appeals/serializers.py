from rest_framework import serializers
from .models import Appeal

class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = '__all__'
