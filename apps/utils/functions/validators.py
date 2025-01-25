from django.core.validators import RegexValidator

uzbek_phone_validator = RegexValidator(
    regex=r"^\+998\d{9}$",
    message="The phone number must be in the Uzbek format (e.g., +998901234567)."
)