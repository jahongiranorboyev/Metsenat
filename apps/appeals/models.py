from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, RegexValidator


class Appeal(models.Model):
    sponsor = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='appeals')
    phone_number = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r"^\+998\d{9}$",
                message="The phone number must be in the Uzbek format (e.g., +998901234567)."
            )
        ]
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
    )
    is_verified = models.BooleanField(default=False)
    payment_method = models.ForeignKey('general.PaymentMethod', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Appeal by {self.sponsor} - {self.amount} UZS"