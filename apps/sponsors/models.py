from decimal import Decimal

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from apps.appeals.models import Appeal
from apps.users.models import UserModel
from apps.utils.models.base_model import AbstractBaseModel


class StudentSponsor(AbstractBaseModel):
   #  Foreign key to the Appeal model representing the appeal linked to this student-sponsor transaction
    appeal = models.ForeignKey(
        'appeals.Appeal',
        on_delete=models.PROTECT,
        related_name='appeal_studentsponsors',
        limit_choices_to={
            'available_balance__gt': 0,
            'status': Appeal.AppealStatus.Approved,
        },
    )
   # Foreign key to the User model representing the student receiving sponsorship
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='student_sponsors',
        limit_choices_to={
            'necessary_balance__gt': 0,
            'role': UserModel.UserRole.STUDENT,
        }
    )
    # The amount of money sponsored to the student
    amount = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('1000000'))],
    )



    def __str__(self):
        """
        String representation of the StudentSponsor model, showing the appeal and student IDs.
        """
        return f"{self.appeal_id} sponsors {self.student_id}"
