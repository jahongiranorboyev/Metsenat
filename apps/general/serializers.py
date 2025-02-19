from rest_framework import serializers
from .models import University
from .models import PaymentMethod
from apps.utils.serializers import BaseModelSerializer


class PaymentMethodSerializer(BaseModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'


class UniversitySerializer(BaseModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


