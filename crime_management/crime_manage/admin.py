from django.contrib import admin
from crime_manage import models

# Register your models here.
admin.site.register(models.InvestigatorProfile)
admin.site.register(models.InvestigatorAddress)
admin.site.register(models.InvestigatorsAdministrativeDetail)