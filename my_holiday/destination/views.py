from django import forms
from django.shortcuts import render
from django.views import generic as views

from my_holiday.accounts.models import Profile
from my_holiday.destination.models import Place
from django.urls import reverse_lazy


def get_profile():
    return Profile.objects.first()


class PlaceCreateView(views.CreateView):
    model = Place
    # from_class = PlaceCreateForm
    fields = ['name', 'location', 'description', 'category', 'rating', 'image_url']
    template_name = 'destination/place_form.html'
    success_url = reverse_lazy('index')
    # TODO redirect must be to 'travelogue_view'


class PlaceDetailView(views.DetailView):
    queryset = Place.objects.all()
    template_name = "destination/place_details.html"
    fields = "__all__"


class PlaceEditView(views.UpdateView):
    pass


class PlaceDeleteView(views.DeleteView):
    pass


def travelogue_view(request):
    has_profile = get_profile()

    places = Place.objects.all() if has_profile else []
    context = {
        "has_profile": has_profile,
        "places": places,
    }

    return render(request, 'destination/travelogue.html', context=context)



