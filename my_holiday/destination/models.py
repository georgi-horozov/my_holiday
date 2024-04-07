from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

UserModel = get_user_model()


class Place(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    CATEGORY_CHOICES = [
        ('Mountain', 'Mountain'),
        ('Sea', 'Sea'),
        ('Historical Site', 'Historical Site'),
        ('City', 'City'),
        ('Spa', 'Spa'),
        ('Wine Tourism', 'Wine Tourism')

    ]
    hotel_name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Hotel name",
    )
    description = models.TextField(
        null=False,
        blank=False,
        verbose_name="Hotel description",
    )
    location = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Hotel location",
    )
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        null=True,
        blank=True,
        verbose_name="Hotel rating",
    )

    image_url = models.ImageField(
        upload_to="mediafiles/photos",
        # validators=[validate_photo_place_size],
        null=True,
        blank=True,
        verbose_name="Hotel photo",
    )

    video = models.FileField(
        upload_to="mediafiles/videos",
        null=True,
        blank=True,
    )

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        null=True,
        blank=True,
        verbose_name="Hotel category",
    )

    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT)








