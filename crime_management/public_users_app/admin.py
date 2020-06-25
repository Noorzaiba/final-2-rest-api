from django.contrib import admin
from public_users_app import models

admin.site.register(models.PublicUser)
admin.site.register(models.PublicUserAddress)
admin.site.register(models.ImageDemo)
