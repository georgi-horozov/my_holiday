from django.http import HttpResponse
from django.shortcuts import render




# from my_holiday.accounts.models import Profile


def index(request):


    context = {

    }

    return render(request, template_name='web/index.html', context=context)

