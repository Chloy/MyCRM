from re import L
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.User


class Skirmish(forms.ModelForm):
    class Meta:
        model = models.Skirmish
        fields = '__all__'
    

class Gangster(forms.ModelForm):
    class Meta:
        model = models.Gangster
        fields = '__all__'