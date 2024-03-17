from django.urls import path, include
from django.contrib.auth import views as auth_views

from my_holiday.accounts.views import LoginUserView, RegisterUserView, logout_user, ProfileDetailsView

urlpatterns = (
    path("login/", LoginUserView.as_view(), name="login user"),
    path("register/", RegisterUserView.as_view(), name="register user"),
    path("logout/", logout_user, name="logout user"),
    path("profile/<int:pk>/", ProfileDetailsView.as_view(), name="details profile"),

)