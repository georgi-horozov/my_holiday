from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class MyCustomPasswordValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(_("The password must contain at least one letter."), code='password_no_letter')
        if not any(char.isdigit() for char in password):
            raise ValidationError(_("The password must contain at least one digit."), code='password_no_digit')
        if not any(char == '_' for char in password):
            raise ValidationError(_("The password must contain at least one underscore."), code='password_no_underscore')

    def get_help_text(self):
        return _("Your password must contain at least one letter, one digit, and one underscore.")


def validate_photo_size(value):
    max_size = 3 * 1024 * 1024

    if value.size > max_size:
        raise ValidationError("The file size exceeds the maximum limit of 3 MB.")


