from ast import Delete
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms


class Home(ListView):
    template_name = 'crm_app/home.html'
    model = models.Gangster
    context_object_name = 'gangsters'


class GangsterDetail(DetailView):
    model = models.Gangster
    template_name = 'crm_app/gangster_detail.html'
    context_object_name = 'gangster'


class GangsterCreate(CreateView):
    model = models.Gangster
    template_name = 'crm_app/gangster_create.html'
    fields = ['firstname', 'lastname']


class GangsterUpdate(UpdateView):
    model = models.Gangster
    fields = ['firstname', 'lastname']
    template_name = 'crm_app/gangster_update.html'


class GangsterDelete(DeleteView):
    model = models.Gangster
    template_name = 'crm_app/gangster_delete.html'
    context_object_name = "gangster"
    success_url = reverse_lazy('crm_app:home')


def gangster_delete(request, pk):
    models.Gangster.objects.get(pk=pk).delete()
    return redirect('/crm')