from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from . import models


class SignUp(CreateView):
    template_name = 'registration/signup.html'
    model = User
    success_url = reverse_lazy('crm_app:login')
    fields = ['username', 'password', 'email', 'is_staff']


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
