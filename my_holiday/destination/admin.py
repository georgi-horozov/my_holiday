from django.contrib import admin

from my_holiday.destination.models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'location', 'rating', 'image_url', 'category']

