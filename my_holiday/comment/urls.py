
from django.urls import path

from my_holiday.comment import views

urlpatterns = (
    path('comment/<int:pk>', views.add_comment, name='comment'),
)