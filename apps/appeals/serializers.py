from rest_framework import serializers
from apps.utils.serializers import BaseModelSerializer
from .models import Appeal


class AppealListCreateSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Appeal
        fields = '__all__'
        read_only_fields = ('status',)


class AppealDetailSerializer(BaseModelSerializer):
    """ 
    Serializer for retrieving, updating, and deleting appeals. 
    `status` field is presented as a choice field.
    """
    status = serializers.ChoiceField(choices=Appeal.AppealStatus.choices)

    class Meta(BaseModelSerializer.Meta):
        model = Appeal
        fields = '__all__'
        read_only_fields = ('status',)
