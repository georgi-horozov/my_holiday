from django.urls import path

from my_holiday.accounts.views import CreateProfileView

urlpatterns = (
    path("create/", CreateProfileView.as_view(), name='create_profile'),
)