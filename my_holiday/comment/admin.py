from django.contrib import admin

from my_holiday.comment.models import Comment


@admin.register(Comment)
class PlaceCommentAdmin(admin.ModelAdmin):
    pass
