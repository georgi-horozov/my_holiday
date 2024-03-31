from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_holiday.web.urls')),
    path('accounts/', include('my_holiday.accounts.urls')),
    path('destination/', include('my_holiday.destination.urls')),
    path('comment/', include('my_holiday.comment.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# handler404 = 'my_holiday.destination.views.error_404'
handler403 = 'my_holiday.destination.views.error_403'

