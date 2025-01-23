from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator



class StudentSponsor(models.Model):
    sponsor = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='sponsored_students')
    student = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='sponsors')
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
    )

    def __str__(self):
        return f"{self.sponsor} sponsors {self.student}"

