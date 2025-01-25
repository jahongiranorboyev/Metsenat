from rest_framework import serializers

from .models import Appeal


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'status')
