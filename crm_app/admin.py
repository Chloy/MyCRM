from django.contrib import admin
from . import models


admin.site.register(models.Gangster)
admin.site.register(models.Gang)
admin.site.register(models.User)
admin.site.register(models.UserProfile)
admin.site.register(models.Skirmish) 