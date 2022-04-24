from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Skirmish(models.Model):
    place = models.CharField(max_length=250)
    participants = models.ManyToManyField('Gangster')
    

class Gang(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    boss = models.OneToOneField('Gangster', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Gangster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    gang_member = models.ForeignKey('Gang', on_delete=models.SET_NULL, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('crm_app:gangster_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)