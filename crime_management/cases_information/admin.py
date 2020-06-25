from django.contrib import admin
from cases_information import models

# Register your models here.
admin.site.register(models.CrimeDetail)
admin.site.register(models.CrimeLocationDetail)
admin.site.register(models.CrimeLiveUpdation)