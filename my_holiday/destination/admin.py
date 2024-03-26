from django.contrib import admin

from my_holiday.destination.models import Place


# @admin.register(Place)
# class PlaceAdmin(admin.ModelAdmin):
#     list_display = ['name', 'description', 'location', 'rating', 'image_url', 'category']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'rating', 'category', 'user')
    list_filter = ('category', 'rating')
    search_fields = ('name', 'location')
    ordering = ('name', '-rating')

    actions = ['custom_action']

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'location', 'rating', 'image_url', 'category', 'user')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('field_name',),
        }),
    )

