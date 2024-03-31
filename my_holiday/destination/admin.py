from django.contrib import admin
from my_holiday.destination.models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'location', 'rating', 'category', 'user')
    list_filter = ('category', 'rating')
    search_fields = ('hotel_name', 'location')
    ordering = ('hotel_name', '-rating')

    actions = ['custom_action']

    fieldsets = (
        (None, {
            'fields': ('hotel_name', 'description', 'location', 'rating', 'image_url', 'category', 'user')
        }),
    )

