
from django.urls import path

from my_holiday.comment import views
from my_holiday.comment.views import like_logic, all_comments_for_place

urlpatterns = (
    path('comment/<int:pk>', views.add_comment, name='comment'),
    path('like/<int:place_id>', like_logic, name='like_logic'),
    path('comments/<int:target_place_id>', all_comments_for_place, name='all_comments'),
)