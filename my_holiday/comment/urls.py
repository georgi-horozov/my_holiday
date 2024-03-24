
from django.urls import path

from my_holiday.comment import views
from my_holiday.comment.views import like_logic

urlpatterns = (
    path('comment/<int:pk>', views.add_comment, name='comment'),
    path('like/<int:place_id>', like_logic, name='like_logic'),
    # path('show_comments_for_place/<int:pk>/', show_comments_for_place, name='show_comments_for_place'),
)