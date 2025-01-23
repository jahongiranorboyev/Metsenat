from enum import Enum

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from decimal import Decimal

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number field is required")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)

class CustomUser(AbstractUser):

    class UserTypeEnum(Enum):
        STUDENT = 'student'
        SPONSOR = 'sponsor'

        @classmethod
        def choices(cls):
            return [(key.value, key.name.capitalize()) for key in cls]

    class DegreeTypeEnum(Enum):
        BACHELOR = 'bachelor'
        MAGISTER = 'magister'

        @classmethod
        def choices(cls):
            return [(key.value, key.name.capitalize()) for key in cls]

    username = None
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^\+998\d{9}$",
                message="The phone number must be in the Uzbek format (e.g., +998901234567)."
            )
        ]
    )
    photo = models.ImageField(
        upload_to='users/%Y/%m/%d',
        blank=True, null=True
    )
    user_type = models.CharField(
        max_length=20,
        choices=UserTypeEnum.choices(),
        default=UserTypeEnum.STUDENT,
        blank=True
    )
    degree = models.CharField(
        max_length=10,
        choices=DegreeTypeEnum.choices(),
        default=DegreeTypeEnum.BACHELOR,
        blank=True
    )
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))],
    )
    university = models.ForeignKey(
        'general.University',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    ordering = ['phone_number']

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
