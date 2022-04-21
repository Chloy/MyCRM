from django import forms
from . import models


class Skirmish(forms.ModelForm):
    class Meta:
        model = models.Skirmish
        fields = '__all__'
    

class Gangster(forms.ModelForm):
    class Meta:
        model = models.Gangster
        fields = '__all__'