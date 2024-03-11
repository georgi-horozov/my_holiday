from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    MOUNTAIN = 'Mountain'
    SEA = 'Sea'
    HISTORICAL_SITE = 'Historical Site'
    CITY = 'City'
    SPA = 'Spa'
    WINE_TOURISM = 'Wine Tourism'

    CATEGORY_CHOICES = [
        (MOUNTAIN, 'Mountain'),
        (SEA, 'Sea'),
        (HISTORICAL_SITE, 'Historical Site'),
        (CITY, 'City'),
        (SPA, 'Spa'),
        (WINE_TOURISM, 'Wine Tourism')

    ]

    name = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        null=False, blank=False,
    )

    def __str__(self):
        return self.name


class Place(models.Model):
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
    address = models.CharField(
        max_length=300,
        null=True,
        blank=True,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_visited = models.DateField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(
        upload_to='photos/',
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    text = models.TextField(
        null=False,
        blank=False,
    )

    rating = models.IntegerField(choices=RATING_CHOICES)
    date_submitted = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
