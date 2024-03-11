from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from my_holiday.accounts.models import Profile


def login(request):
    pass


def logout(request):
    pass


class CreateProfileView(views.CreateView):
    queryset = Profile.objects.all()
    template_name = "accounts/create_profile.html"
    fields = ["username", "password", "email", "age", "first_name", "last_name"]
    success_url = reverse_lazy("index") #ще отива към travelogue

