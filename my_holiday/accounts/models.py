from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import models as auth_models
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from my_holiday.accounts.managers import MyHolidayUserManager
from my_holiday.accounts.validators import validate_password


class MyHolidayUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = "email"

    objects = MyHolidayUserManager()


class Profile(models.Model):
    MAX_LENGTH_FIRST_NAME = 50
    MAX_LENGTH_LAST_NAME = 50

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        null=True,
        blank=True,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        null=True,
        blank=True,
        verbose_name='Last Name',
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Age',
    )

    profile_photo = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Photo',
    )

    user = models.OneToOneField(
        MyHolidayUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )









