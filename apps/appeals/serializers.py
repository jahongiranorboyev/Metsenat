from rest_framework import serializers

from apps.utils.serializers import BaseModelSerializer

from .models import Appeal


class AppealSerializer(BaseModelSerializer):
    sponsor = serializers.SerializerMethodField()
    payment_method = serializers.SerializerMethodField()

    class Meta(BaseModelSerializer.Meta):
        model = Appeal
        fields = [
            'id',
            'sponsor',
            'sponsor_fullname',
            'status',
            'phone_number',
            'payment_method',
            'amount',
            'available_balance'
        ]
        read_only_fields = ('status',)

    def get_sponsor(self, obj):
        """
        retruns all sponsor names
        """
        return obj.sponsor.full_name if obj.sponsor else None

    def get_payment_method(self, obj):
        """
        retruns all payment names
        """
        return obj.payment_method.name if obj.payment_method else None
