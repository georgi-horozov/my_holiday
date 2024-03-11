from django.db import models

from my_holiday.accounts.valodators import validator_username, validate_username_length


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 20

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(validator_username, validate_username_length,),
        null=False,
        blank=False,
        verbose_name='Username',
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Password',
    )

    email = models.EmailField(
        null=False,
        blank=False,
        verbose_name='Email',
    )

    first_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Last Name',
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Age',
    )

    profile_photo = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Photo',
    )







