from django.shortcuts import redirect, render
from django.views.generic import ListView
from . import models
from . import forms


class Home(ListView):
    template_name = 'crm_app/home.html'
    queryset = models.Gangster.objects.all()
    context_object_name = 'gangsters'


def gangster_detail(request, pk):
    context = {
        'gangster': models.Gangster.objects.get(pk=pk)
    }
    return render(request, 'crm_app/gangster_detail.html', context)


def gangster_create(request):
    form = forms.Gangster()
    if request.method == 'POST':
        form = forms.Gangster(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'crm_app/gangster_create.html', context)


def gangster_update(request, pk):
    gangster = models.Gangster.objects.get(pk=pk)
    form = forms.Gangster(instance=gangster)
    if request.method == 'POST':
        form = forms.Gangster(request.POST, instance=gangster)
        if form.is_valid:
            form.save()
    context = {
        'gangster': gangster,
        'form': form
    }
    return render(request, 'crm_app/gangster_update.html', context)


def gangster_delete(request, pk):
    models.Gangster.objects.get(pk=pk).delete()
    return redirect('/crm')