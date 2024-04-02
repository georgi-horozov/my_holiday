from django.contrib.auth import views as auth_views, login, logout
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from my_holiday.accounts.forms import MyHolidayUserCreationForm
from my_holiday.accounts.models import Profile
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Profile
from ..destination.models import Place

from django.contrib.auth.mixins import AccessMixin

## нещо не работи
# class OwnerRequiredMixin(AccessMixin):
#     def dispatch(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         profile = get_object_or_404(Profile, pk=pk)
#
#         if request.user != profile.user:
#             return self.handle_no_permission()
#
#         return super().dispatch(request, *args, **kwargs)


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


class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = 'accounts/edit_profile.html'
    fields = ("first_name", "last_name", "age", "profile_photo",)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            self.object.first_name = form.cleaned_data['first_name']
            self.object.last_name = form.cleaned_data['last_name']
            self.object.age = form.cleaned_data['age']

            profile_photo = request.FILES.get('profile_photo')
            if profile_photo:
                self.object.profile_photo = profile_photo

            self.object.save()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse("details profile", kwargs={"pk": self.object.pk})


class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'accounts/delete_profile.html'

    success_url = reverse_lazy("index")







