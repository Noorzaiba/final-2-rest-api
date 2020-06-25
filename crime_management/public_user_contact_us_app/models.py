from django.db import models
from public_users_app.models import PublicUser

# Create your models here.

class QueryModel(models.Model):
    email=models.ForeignKey(PublicUser,on_delete=models.CASCADE)
    description=models.CharField(max_length=1000)
    status=models.CharField(max_length=1000)
    doc=models.DateTimeField(auto_now_add=True,blank=True)
    dou=models.DateTimeField(auto_now=True,blank=True)

       
    def __str__(self):
        return self.email.email_id