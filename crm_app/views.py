from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models


class UserProfile(TemplateView):
    form_class = forms.UserProfile
    template_name = 'crm_app/user_profile.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        profile = models.UserProfile.objects.get(user__id=self.request.user.id)
        data['username'] = profile.user.username
        data['gangster'] = f'{profile.gangster.firstname} {profile.gangster.lastname}'
        if profile.gangster.gang_member:
            data['gang'] = profile.gangster.gang_member.name
        return data


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
    model = models.Gang
    fields = ['name']
    content_object_name = 'gang'


class GangDelete(LoginRequiredMixin, DeleteView):
    template_name = 'crm_app/gang_delete.html'
    model = models.Gang
    success_url = reverse_lazy('crm_app:gangs')


class Home(ListView):
    template_name = 'crm_app/home.html'
    model = models.Skirmish
    context_object_name = 'skirmishs'


class GangsterDetail(LoginRequiredMixin, DetailView):
    model = models.Gangster
    template_name = 'crm_app/gangster_detail.html'
    context_object_name = 'gangster'