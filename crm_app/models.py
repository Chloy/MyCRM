from django.db import models

class Skirmish(models.Model):
    place = models.CharField(max_length=250)
    participants = models.ManyToManyField('Gangster')
    

class Gangster(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)