from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models


class SignUp(CreateView):
    template_name = 'registration/signup.html'
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('crm_app:login')


class CreateSkirmish(LoginRequiredMixin, CreateView):
    template_name = 'crm_app/skirmish_create.html'
    form_class = forms.SkirmishForm
    content_object_name = 'skirmish'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(request)
        return redirect(reverse_lazy('crm_app:home'))


class Gangs(ListView):
    template_name = 'crm_app/gangs.html'
    model = models.Gang


class GangCreate(LoginRequiredMixin, CreateView):
    template_name = 'crm_app/gang_create.html'
    form_class = forms.GangForm

    def post(self, request, *args, **kwargs):
        form = forms.GangForm(request.POST)
        if form.is_valid():
            form.save(request)
        return redirect(reverse_lazy('crm_app:home'))


class GangDetail(DetailView):
    template_name = 'crm_app/gang_detail.html'
    model = models.Gang
    content_object_name = 'gang'


class GangUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'crm_app/gang_update.html'
    form_class = forms.GangForm
    content_object_name = 'gang'


class GangDelete(LoginRequiredMixin, DeleteView):
    template_name = 'crm_app/gang_delete.html'
    form_class = forms.GangForm
    content_object_name = 'gang'


class Home(ListView):
    template_name = 'crm_app/home.html'
    model = models.Skirmish
    context_object_name = 'skirmishs'


class GangsterDetail(LoginRequiredMixin, DetailView):
    model = models.Gangster
    template_name = 'crm_app/gangster_detail.html'
    context_object_name = 'gangster'


# class GangsterCreate(LoginRequiredMixin, CreateView):
#     template_name = 'crm_app/gangster_create.html'
#     form_class = forms.GangsterForm

#     def post(self, request, *args, **kwargs):
#         form = forms.GangsterForm(request.POST)
#         if form.is_valid():
#             form.save(request)
#         return redirect(reverse_lazy('crm_app:home'))


# class GangsterUpdate(LoginRequiredMixin, UpdateView):
#     model = models.Gangster
#     fields = ['firstname', 'lastname']
#     template_name = 'crm_app/gangster_update.html'


# class GangsterDelete(LoginRequiredMixin, DeleteView):
#     model = models.Gangster
#     template_name = 'crm_app/gangster_delete.html'
#     context_object_name = "gangster"
#     success_url = reverse_lazy('crm_app:home')