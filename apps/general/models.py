from decimal import Decimal

from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from apps.utils.models.base_model import AbstractBaseModel


class PaymentMethod(AbstractBaseModel):
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter the name of the payment method."
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        blank=True,
        editable=False,
        help_text="Slug will be automatically generated based on the name if left blank."
    )

    def clean(self):
        # If slug is not provided, generate it automatically from the name
        if not self.slug:
            self.slug = slugify(self.name)

        # Check if the slug is unique
        if PaymentMethod.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            raise ValidationError(f"The slug '{self.slug}' is already taken.")

    def save(self, *args, **kwargs):
        # Call clean to ensure slug is validated/created
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class University(AbstractBaseModel):
    name = models.CharField(
        max_length=100,
        verbose_name="University Name"
    )
    contract_amount = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Contract Amount"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        editable=False,
    )
    def clean(self):
        # If slug is not provided, generate it automatically from the name
        self.slug = slugify(self.name)
        # Check if the slug is unique
        if University.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            raise ValidationError(f"The slug '{self.slug}' is already taken.")

    def save(self, *args, **kwargs):
        """
        Overriding save to validate and assign the slug field.
        """
        self.clean()
        if self.pk :
            old_instance = University.objects.get(pk=self.pk)
            if self.contract_amount != old_instance.contract_amount:
                raise ValidationError({"Contract amount must be unchangeable!"})
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
