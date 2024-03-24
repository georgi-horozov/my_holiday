from django.contrib.auth import get_user_model
from django.db import models

from my_holiday.destination.models import Place

UserModel = get_user_model()
class Comment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(max_length=MAX_TEXT_LENGTH)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_place = models.ForeignKey(Place, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
