from decimal import Decimal

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

from apps.users.models import UserModel
from apps.utils.models.base_model import AbstractBaseModel
from apps.utils.functions.validators import uzbek_phone_validator
from apps.utils.functions.validators import check_fullname

class Appeal(AbstractBaseModel):
    """
    Model for representing an appeal made by a sponsor.
    """
    class AppealStatus(models.TextChoices):
        """
        Enumeration for the possible statuses of an appeal.
        """
        New = 'new', 'New'
        Approved = 'approved', 'Approved'
        Reviewing = 'reviewing...', 'Reviewing...'
        Cancelled = 'cancelled', 'Cancelled'

    sponsor_fullname = models.CharField(
	max_length=50,
	validators=[check_fullname]
    )
    sponsor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='appeals',
        limit_choices_to={
            'role': UserModel.UserRole.SPONSOR
        },
    )
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        validators=[uzbek_phone_validator]
    )
    amount = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('1000000'))]
    )
    available_balance = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))],
        blank=True,
        null=True,
        editable=False
    )
    status = models.CharField(
        max_length=20,
        choices=AppealStatus.choices,
        default=AppealStatus.New,

    )
    payment_method = models.ForeignKey(
        'general.PaymentMethod',
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = 'Appeal'
        verbose_name_plural = 'Appeals'
        unique_together = (('sponsor', 'phone_number'),)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.available_balance = self.amount
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sponsor_fullname
