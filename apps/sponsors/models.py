from decimal import Decimal

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.db.models import Sum

from apps.appeals.models import Appeal
from apps.utils.models.base_model import AbstractBaseModel


class StudentSponsor(AbstractBaseModel):
    # Foreign key to the Appeal model representing the appeal linked to this student-sponsor transaction
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
        related_name='student_studentsponsors',
    )
    # The amount of money sponsored to the student
    amount = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))],
    )

    def clean(self):
        """
        Custom validation method to ensure that:
        - The sponsored amount is not greater than the available balance of the appeal.
        - The sponsored amount is not greater than the student's available balance.
        """
        if self.amount > self.appeal.available_balance:
            raise ValidationError({'message': 'Amount cannot be greater than the appeal available balance.'})
        if self.amount > self.student.balance:
            raise ValidationError({'message': 'Amount cannot be greater than the student\'s available balance.'})

    def save(self, *args, **kwargs):
        """
        Overridden save method to perform the following actions:
        - Update the available balance of the appeal after sponsorship.
        - Deduct the sponsored amount from the student's balance.
        - Update the sponsor's total available funds by calculating the sum of all their related appeals' available balances.
        """
        # Update available balance of the appeal by deducting the sponsorship amount
        self.appeal.available_balance -= self.amount
        self.appeal.save(update_fields=['available_balance'])

        # Update the student's balance by deducting the sponsorship amount
        self.student.balance -= self.amount
        self.student.save(update_fields=['balance'])

        # Call the parent save method to store the StudentSponsor object
        super().save(*args, **kwargs)

        # Update the sponsor's total available funds by summing the available balances of all their approved appeals
        self.appeal.sponsor.available_balance = self.appeal.sponsor.appeals.aggregate(
            Sum('available_balance'))['available_balance__sum'] or 0

    def __str__(self):
        """
        String representation of the StudentSponsor model, showing the appeal and student IDs.
        """
        return f"{self.appeal_id} sponsors {self.student_id}"
