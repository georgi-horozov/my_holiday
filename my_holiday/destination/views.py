from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic as views
from my_holiday.comment.forms import CommentForm
from my_holiday.comment.models import Like
from my_holiday.destination.forms import PlaceCreateForm, PlaceEditForm
from my_holiday.destination.models import Place
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden


@method_decorator(login_required, name='dispatch')
class PlaceCreateView(views.CreateView):
    form_class = PlaceCreateForm
    model = Place
    template_name = 'destination/place_form.html'
    success_url = reverse_lazy('travelogue_view')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.image_url = self.request.FILES.get('image_url')
        self.object.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.instance.image_url = request.FILES.get('image_url')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class PlaceDetailView(views.DetailView):
    queryset = Place.objects.all()
    template_name = "destination/place_details.html"
    fields = "__all__"


@method_decorator(login_required, name='dispatch')
class PlaceEditView(views.UpdateView):
    queryset = Place.objects.all()
    template_name = "destination/place_edit.html"
    form_class = PlaceEditForm
    success_url = reverse_lazy('travelogue_view')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return render(request, '403.html', {'message': 'You do not have permission to edit this place.'}, status=403)
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class PlaceDeleteView(views.DeleteView):
    queryset = Place.objects.all()
    template_name = "destination/place_delete.html"
    success_url = reverse_lazy('travelogue_view')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return render(request, '403.html', {'message': 'You do not have permission to delete this place.'}, status=403)
        return super().dispatch(request, *args, **kwargs)


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


def error_403(request, exception):
    return render(request, '403.html', status=403)






