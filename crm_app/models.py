from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Skirmish(models.Model):
    place = models.CharField(max_length=250)
    participants = models.ManyToManyField('Gangster')
    gangs = models.ManyToManyField('Gang')
    

class Gang(models.Model):
    name = models.CharField(max_length=250)
    boss = models.OneToOneField('Gangster', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Gangster(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    gang_member = models.ForeignKey('Gang', on_delete=models.SET_NULL, null=True, blank=True)


    def get_absolute_url(self):
        return reverse('crm_app:gangster_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# def post_gangster_created_signal(self, instance, created, **kwardgs):
#     if created:
#         instance.user = 



post_save.connect(post_user_created_signal, sender=User)
# post_save.connect(post_user_created_signal, sender=Gangster)