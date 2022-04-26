from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.User


class SkirmishForm(forms.ModelForm):
    class Meta:
        model = models.Skirmish
        fields = '__all__'
    

class GangsterForm(forms.ModelForm):
    class Meta:
        model = models.Gangster
        fields = '__all__'
        exclude = ('user',)

    def save(self, request):
        gangster = super(GangsterForm, self).save(commit=False)
        gangster.user = request.user
        gangster.save()