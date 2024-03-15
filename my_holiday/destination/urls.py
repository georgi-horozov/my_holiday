from django.urls import path

from my_holiday.destination.views import PlaceCreateView, travelogue_view, PlaceDetailView

urlpatterns = (
    path("create/", PlaceCreateView.as_view(), name='create_place'),
    path("travelogue/", travelogue_view, name="travelogue_view"),
    path("<int:pk>/details/", PlaceDetailView.as_view(), name="details_place"),
)


