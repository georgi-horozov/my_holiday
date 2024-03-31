from django import forms
from my_holiday.destination.models import Place

class PlaceBaseForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['hotel_name', 'description', 'location', 'rating', 'image_url', 'category',]
        widgets = {
            'hotel_name': forms.TextInput(attrs={'placeholder': 'Enter hotel name...'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter short hotel description...'}),
            'location': forms.TextInput(attrs={'placeholder': 'Fill hotel location...'}),

        }

class PlaceCreateForm(PlaceBaseForm):
    pass


class PlaceDetailsForm(PlaceBaseForm):
    pass

class PlaceEditForm(PlaceBaseForm):
    pass








