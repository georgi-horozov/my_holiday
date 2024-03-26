from django import forms
from my_holiday.destination.models import Place

from django import forms
from my_holiday.destination.models import Place

class PlaceBaseForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'description', 'location', 'rating', 'image_url', 'category',]

class PlaceCreateForm(PlaceBaseForm):
    pass


class PlaceDetailsForm(PlaceBaseForm):
    pass

class PlaceEditForm(PlaceBaseForm):
    pass






