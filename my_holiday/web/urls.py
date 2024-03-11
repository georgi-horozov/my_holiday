from django.urls import path

from my_holiday.web.views import index

urlpatterns = (
    path('', index, name='index'),
)