from django.contrib import admin

from my_holiday.comment.models import Comment, Like


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_time_of_publication', 'to_place',)
    search_fields = ('text',)
    list_filter = ('date_time_of_publication',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('to_place', 'user',)
    search_fields = ('to_place',)
    list_filter = ('user',)

