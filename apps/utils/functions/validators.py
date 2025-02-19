from django.core.validators import RegexValidator

uzbek_phone_validator = RegexValidator(
    regex=r"^\+998\d{9}$",
    message="The phone number must be in the Uzbek format (e.g., +998901234567)."
)

def check_fullname(fullname):
    # Split the name into parts
    parts = fullname.split()

    # Ensure there are exactly two parts (first name and surname)
    if len(parts) != 2:
        raise ValidationError(f"{fullname} must contain both a first name and a surname.")

    surname, name = parts

    # Ensure both parts contain only letters
    if not surname.isalpha() or not name.isalpha():
        raise ValidationError(f"{fullname} must only contain letters.")
