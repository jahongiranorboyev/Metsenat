from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=100)
    contract_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
    )

    def __str__(self):
        return self.name