from django.core.exceptions import ValidationError


def validator_username(value):
    for char in value:
        if not char.isalnum() and char != "_":
            raise ValidationError("Username must contain only letters, digits, and underscores!")


def validate_username_length(value):
    if len(value) < 5:
        raise ValidationError("Username must be at least 5 chars long!")
