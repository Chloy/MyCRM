from django.shortcuts import render
from . import models


def home(request):
    gangsters = models.Gangster.objects.all()
    context = {
        'gangsters': gangsters
    }
    return render(request, 'crm_app/home.html', context)


def gangster_detail(request, pk):
    context = {
        'gangster': models.Gangster.objects.get(pk=pk)
    }
    return render(request, 'crm_app/gangster_detail.html', context)