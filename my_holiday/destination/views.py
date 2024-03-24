from django import forms
from django.shortcuts import render
from django.views import generic as views

from my_holiday.accounts.models import Profile, MyHolidayUser
from my_holiday.comment.forms import CommentForm
from my_holiday.comment.models import Like
from my_holiday.destination.forms import PlaceCreateForm, PlaceEditForm
from my_holiday.destination.models import Place
from django.urls import reverse_lazy, reverse


def get_profile():
    return Profile.objects.first()


class PlaceCreateView(views.CreateView):
    form_class = PlaceCreateForm
    model = Place

    # fields = ['name', 'location', 'description', 'category', 'rating', 'image_url']
    template_name = 'destination/place_form.html'
    success_url = reverse_lazy('travelogue_view')



    def form_valid(self, form):
        place = form.save(commit=False)
        place.user = self.request.user
        place.save()
        return super().form_valid(form)


class PlaceDetailView(views.DetailView):
    queryset = Place.objects.all()
    template_name = "destination/place_details.html"
    fields = "__all__"


class PlaceEditView(views.UpdateView):
    queryset = Place.objects.all()
    template_name = "destination/place_edit.html"
    form_class = PlaceEditForm
    success_url = reverse_lazy('travelogue_view')


class PlaceDeleteView(views.DeleteView):
    queryset = Place.objects.all()
    template_name = "destination/place_delete.html"
    success_url = reverse_lazy('travelogue_view')



def travelogue_view(request):
    places = Place.objects.all()
    places_with_email = []
    comment_form = CommentForm()

    for place in places:
        user_email = place.user.email if place.user else None
        liked_place = Like.objects.filter(to_place=place, user=request.user).exists() if request.user.is_authenticated else False
        places_with_email.append({'place': place, 'user_email': user_email, 'liked_place': liked_place})

    context = {
        "places_with_email": places_with_email,
        "comment_form": comment_form,
    }

    return render(request, 'destination/travelogue.html', context=context)





