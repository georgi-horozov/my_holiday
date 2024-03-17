from django.contrib.auth import views as auth_views, login, logout
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from my_holiday.accounts.forms import MyHolidayUserCreationForm
from my_holiday.accounts.models import Profile
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Profile
from ..destination.models import Place


class LoginUserView(auth_views.LoginView):
    template_name = "accounts/login_user.html"


class RegisterUserView(views.CreateView):
    template_name = "accounts/register_user.html"
    form_class = MyHolidayUserCreationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result


def logout_user(request):
    logout(request)
    return redirect('login user')




class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/details_profile.html'
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Get the current user's profile
    #     profile = self.object
    #     # Count the total number of places (or photos) associated with the user
    #     place_count = Place.objects.filter(user=profile.user).count()
    #     # Add the place count to the context
    #     context['place_count'] = place_count
    #     return context




