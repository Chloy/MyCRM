from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    gangster = models.OneToOneField('Gangster', on_delete=models.SET_NULL, null=True)


class Skirmish(models.Model):
    place = models.CharField(max_length=250)
    gangs = models.ManyToManyField('Gang')


class Gang(models.Model):
    name = models.CharField(max_length=250)
    boss = models.OneToOneField('Gangster', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('crm_app:gang_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Gangster(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    gang_member = models.ForeignKey('Gang', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(default='guts.png')

    def get_absolute_url(self):
        return reverse('crm_app:gangster_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def save(self):
        super().save()
        try:
            img = Image.open(self.image.path)
        except:
            pass
        else:
            if img.height > 300 or img.width > 300:
                size = (300, 300)
                img.thumbnail(size)
                img.save(self.image.path)


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        firsname, *lastname = instance.username.split()
        gangster = Gangster.objects.create(
            user=instance,
            firstname=firsname,
            lastname=''.join(lastname)
        )
        UserProfile.objects.create(user=instance, gangster=gangster)


post_save.connect(post_user_created_signal, sender=User)