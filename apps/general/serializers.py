from rest_framework import serializers

from .models import University
from .models import PaymentMethod
from apps.utils.serializers import BaseModelSerializer


class PaymentMethodSerializer(BaseModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id','name','created_at','updated_at']


class UniversitySerializer(BaseModelSerializer):

    class Meta:
        model = University
        fields = ['id','name','contract_amount','created_at','updated_at']



