from django.db import models
from public_users_app.models import PublicUser

# Create your models here.


class PasswordRestForPublicUsers(models.Model):
    otp=models.CharField(null=True,blank=True,max_length=8)
    email=models.CharField(max_length=200)
    status=models.BooleanField(default=False)


    def __str__(self):
        return self.email