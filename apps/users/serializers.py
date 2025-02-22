from rest_framework import serializers
from apps.utils.serializers import BaseModelSerializer
from .models import UserModel
from ..appeals.models import Appeal
from ..sponsors.models import StudentSponsor
from ..sponsors.serializers import StudentSponsorSerializer


class CustomUserCreateSerializer(BaseModelSerializer):
    """
    Serializer for CustomUser model. Handles validation and serialization of user data.
    """
    university = serializers.SerializerMethodField()
    role = serializers.ChoiceField(choices=UserModel.UserRole.choices)

    class Meta:
        model = UserModel
        fields = [
            'id',
            'full_name',
            'photo',
            'phone_number',
            'role',
            'degree',
            'university',
            'necessary_balance',
            'available_balance',
            'sponsor_type',
            'total_balance'
        ]
        read_only_fields = ['total_balance', 'available_balance', 'necessary_balance']

    def get_university(self, obj):
        """
        returns the university name instead of id
        """
        return obj.university.name if obj.university else None


class CustomUserDetailSerializer(serializers.ModelSerializer):
    university = serializers.SerializerMethodField()
    sponsor_appeals = serializers.SerializerMethodField()
    student_appeals = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = [
            'id',
            'full_name',
            'photo',
            'phone_number',
            'role',
            'degree',
            'university',
            'necessary_balance',
            'available_balance',
            'sponsor_type',
            'total_balance',
            'sponsor_appeals',
            'student_appeals'
        ]
        read_only_fields = ['total_balance', 'available_balance', 'necessary_balance']

    def get_sponsor_appeals(self, obj):
        """
        returns all appeals involving the sponsor
        """
        from apps.appeals.serializers import AppealSerializer
        appeals = Appeal.objects.filter(sponsor_id=obj.pk)
        return AppealSerializer(appeals, many=True).data

    def get_student_appeals(self, obj):
        """
        returns all appeals involving the sponsor
        """
        sponsors = StudentSponsor.objects.filter(student_id=obj.pk)
        return StudentSponsorSerializer(sponsors, many=True).data

    def get_university(self, obj):
        """
        returns university name instead of id
        """
        return obj.university.name if obj.university else None

    def get_fields(self):
        """Dynamically modify fields based on the user's role and requested UUID."""
        fields = super().get_fields()
        request = self.context.get('request')
        view = self.context.get('view')

        if request and hasattr(request, 'user'):
            user = request.user
            requested_user = None

            if view and hasattr(view, 'kwargs'):
                user_uuid = view.kwargs.get('pk')
                if user_uuid:
                    try:
                        requested_user = UserModel.objects.get(id=user_uuid)
                    except UserModel.DoesNotExist:
                        requested_user = None

            if requested_user and user == requested_user:
                pass

            elif requested_user and requested_user.role == UserModel.UserRole.STUDENT:
                fields.pop('available_balance', None)
                fields.pop('sponsor_type', None)
                fields.pop('sponsor_appeals', None)

            elif requested_user and requested_user.role == UserModel.UserRole.SPONSOR:
                fields.pop('degree', None)
                fields.pop('university', None)
                fields.pop('necessary_balance', None)
                fields.pop('student_appeals', None)

            elif requested_user and requested_user.role == UserModel.UserRole.ADMIN:
                fields.pop('available_balance', None)
                fields.pop('sponsor_type', None)
                fields.pop('total_balance', None)
                fields.pop('degree', None)
                fields.pop('university', None)
                fields.pop('necessary_balance', None)
                fields.pop('student_appeals', None)
                fields.pop('sponsor_appeals', None)


        return fields
