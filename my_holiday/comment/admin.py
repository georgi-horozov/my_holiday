from django.contrib import admin

from my_holiday.comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_time_of_publication', 'to_place',)
    search_fields = ('text',)
    list_filter = ('date_time_of_publication',)
