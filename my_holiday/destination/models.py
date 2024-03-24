from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

UserModel = get_user_model()

class Place(models.Model):
    RATING_CHOICES = [
        ('1 Star', '1 Star'),
        ('2 Stars', '2 Stars'),
        ('3 Stars', '3 Stars'),
        ('4 Stars', '4 Stars'),
        ('5 Stars', '5 Stars'),
    ]

    CATEGORY_CHOICES = [
        ('Mountain', 'Mountain'),
        ('Sea', 'Sea'),
        ('Historical Site', 'Historical Site'),
        ('City', 'City'),
        ('Spa', 'Spa'),
        ('Wine Tourism', 'Wine Tourism')

    ]
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    location = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        unique=True,
        default="https://...",
        verbose_name="Image URL",
        error_messages={
            'unique': "This image URL is already in use! Provide a new one."
        }
    )
    

    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)

    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT)









