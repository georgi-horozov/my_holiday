from django.http import HttpResponse
from django.shortcuts import render

# from my_holiday.accounts.models import Profile


def index(request):
    # has_profile = Profile.objects.first()
    # context = {
    #     "has_profile": has_profile,
    # }

    return render(request, template_name='web/index.html',)

