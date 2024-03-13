from django import forms
from django.shortcuts import render
from django.views import generic as views


from my_holiday.destination.models import Place
from django.urls import reverse_lazy


class PlaceCreateView(views.CreateView):
    model = Place
    # from_class = PlaceCreateForm
    fields = ['name', 'location', 'description', 'category', 'rating', 'image']
    template_name = 'destination/place_form.html'
    success_url = reverse_lazy('index')
    # TODO redirect must be to 'travelogue_view'

# from django.views import generic as views
# from my_holiday.destination.models import Place
# from django.urls import reverse_lazy
#
# class PlaceCreateView(views.CreateView):
#     model = Place
#     form_class = PlaceForm  # Use the custom form
#     template_name = 'destination/place_form.html'
#     success_url = reverse_lazy('index')
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         # Provide choices for the rating field
#         kwargs['rating_choices'] = Place.RATING_CHOICES
#         return kwargs

