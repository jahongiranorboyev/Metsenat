from decimal import Decimal
from django.contrib.auth.models import AbstractUser,User,BaseUserManager

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MinValueValidator
from django.db.models import Q

from apps.general.models import University
from apps.utils.functions import uzbek_phone_validator
from apps.utils.models.base_model import AbstractBaseModel


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


class CustomUser(AbstractUser, AbstractBaseModel):
    class UserRole(models.TextChoices):
        STUDENT = 'student', 'Student'
        SPONSOR = 'sponsor', 'Sponsor'
        ADMIN = 'admin', 'Admin'

    class StudentDegree(models.TextChoices):
        BACHELOR = 'bachelor', 'Bachelor'
        MAGISTER = 'magister', 'Magister'

    class SponsorType(models.TextChoices):
        PHYSICAL = 'physical', 'Physical'
        LEGAL = 'legal', 'Legal'

    full_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    username = None
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        validators=[uzbek_phone_validator]
    )
    photo = models.ImageField(
        upload_to='users/%Y/%m/%d',
        blank=True,
        null=True
    )
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
    )
    degree = models.CharField(
        max_length=10,
        choices=StudentDegree.choices,  
        blank=True,
        null=True
    )
    necessary_balance = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=Decimal('0'),
        validators=[MinValueValidator(Decimal('0'))],
        blank=True,
        null=True,
        editable=False
    )
    available_balance = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=Decimal('0'),
        validators=[MinValueValidator(Decimal('0'))],
        blank=True,
        null=True,
        editable=False
    )
    total_balance = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=Decimal('0'),
        validators=[MinValueValidator(Decimal('0'))],
        blank=True,
        null=True,
        editable=False
    )
    university = models.ForeignKey(
        University,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    sponsor_type = models.CharField(
        max_length=20,
        choices=SponsorType.choices,
        blank=True,
        null=True
    )
    telegram_id = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )

    objects = CustomUserManager()
    USERNAME_FIELD = 'phone_number'

    def add_group(self):
        group, created = Group.objects.get_or_create(name=self.role)
        if created:
            match self.role:
                case UserModel.UserRole.ADMIN:
                    perms = Permission.objects.all()
                case UserModel.UserRole.SPONSOR:
                    perms = Permission.objects.filter(
                        Q(codename__startswith='view_')
                        |
                        Q(codename__in=['change_appeal', 'add_appeal', 'delete_appeal'])
                    )
                case UserModel.UserRole.STUDENT:
                    perms = Permission.objects.filter(codename__startswith='view_')
                case _:
                    perms = []

            group.permissions.set(perms)
        self.groups.set([group])
        return group

    def clean(self):
        if self.role == UserModel.UserRole.SPONSOR and any([self.degree, self.university]):
            raise ValidationError({
                "Degree and University are not allowed in sponsor"
            })

        if self.role != self.UserRole.SPONSOR and self.sponsor_type:
            raise ValidationError({"sponsor_type": "This field is required in only sponsor "})
        #
        # if self.role == self.UserRole.SPONSOR and self.sponsor_type is None:
        #     raise ValidationError({"sponsor_type": "This field is required "})

        if self.role == self.UserRole.STUDENT and (not self.university or not self.degree):
            raise ValidationError({
                'university': 'The university is required',
                'degree': 'The degree is required',
            })

        if self.role == UserModel.UserRole.ADMIN and any([self.degree, self.university, self.sponsor_type]):
            raise ValidationError(
                {
                "degree": "degree is not required",
                "university": "university is not required",
                "sponsor_type": "sponsor type is not required"
                }
            )

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = UserModel.UserRole.ADMIN
        self.clean()
        if self.role == self.UserRole.STUDENT:
            if not self.pk:
                self.necessary_balance = self.university.contract_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone_number


UserModel = CustomUser
