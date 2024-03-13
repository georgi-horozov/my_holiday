from django.urls import path

from my_holiday.destination.views import PlaceCreateView

urlpatterns = (
    path("create/", PlaceCreateView.as_view(), name='create_place'),
)