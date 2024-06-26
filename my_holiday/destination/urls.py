from django.urls import path

from my_holiday.destination.views import PlaceCreateView, travelogue_view, PlaceDetailView, PlaceEditView, \
    PlaceDeleteView

urlpatterns = [
    path("create/", PlaceCreateView.as_view(), name='create_place'),
    path("<int:pk>/edit/", PlaceEditView.as_view(), name='edit_place'),
    path("<int:pk>/delete/", PlaceDeleteView.as_view(), name="delete place"),
    path("travelogue/", travelogue_view, name="travelogue_view"),

]


