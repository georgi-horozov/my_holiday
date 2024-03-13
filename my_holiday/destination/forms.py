# from django import forms
# from my_holiday.destination.models import Place
#
# class PlaceForm(forms.ModelForm):
#     rating = forms.ChoiceField(choices=Place.RATING_CHOICES)
#     category = forms.ModelChoiceField(queryset=Category.objects.all())
#
#     class Meta:
#         model = Place
#         fields = ['name', 'location', 'description', 'category', 'rating', 'image']
#
#     def __init__(self, *args, **kwargs):
#         rating_choices = kwargs.pop('rating_choices', None)
#         super().__init__(*args, **kwargs)
#         if rating_choices:
#             self.fields['rating'] = forms.ChoiceField(choices=rating_choices)




