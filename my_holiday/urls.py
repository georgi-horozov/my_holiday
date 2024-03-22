from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_holiday.web.urls')),
    path('accounts/', include('my_holiday.accounts.urls')),
    path('destination/', include('my_holiday.destination.urls')),
    path('comment/', include('my_holiday.comment.urls')),
]
