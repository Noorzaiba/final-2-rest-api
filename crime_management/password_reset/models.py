from django.db import models
from crime_manage.models import InvestigatorProfile

# Create your models here.


class PasswordRest(models.Model):
    otp=models.CharField(null=True,blank=True,max_length=8)
    email=models.CharField(max_length=200)
    status=models.BooleanField(default=False)


    def __str__(self):
        return self.email