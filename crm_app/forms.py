from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.User


class SkirmishForm(forms.ModelForm):
    class Meta:
        model = models.Skirmish
        fields = ['enemy_gang', 'place']

    enemy_gang = forms.ModelChoiceField(models.Gang.objects.all())
    place = forms.CharField(max_length=250)

    def save(self, request):
        skirmish = super(SkirmishForm, self).save(commit=False)
        # skirmish.gangs.add(request.user__userprofile)


class GangsterForm(forms.ModelForm):
    class Meta:
        model = models.Gangster
        fields = '__all__'
        exclude = ('user',)

    def save(self, request):
        gangster = super(GangsterForm, self).save(commit=False)
        gangster.user = request.user
        gangster.save()


class GangForm(forms.ModelForm):
    class Meta:
        model = models.Gang
        fields = '__all__'
        exclude = ('boss',)

    def save(self, request):
        gang = super(GangForm, self).save(commit=False)
        gang.boss = models.Gangster.objects.get(user=request.user.id)
        gang.save()