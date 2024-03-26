from django.core.exceptions import ValidationError


def validate_password(password):
    if len(password) < 6:
        raise ValidationError("Password must be at least 6 characters long.")

    has_letter = False
    has_digit = False
    has_underscore = False

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
        elif char == '_':
            has_underscore = True

    if not has_letter:
        raise ValidationError("Password must contain at least one letter.")

    if not has_digit:
        raise ValidationError("Password must contain at least one digit.")

    if not has_underscore:
        raise ValidationError("Password must contain at least one underscore.")
