from django.db import models
from crime_manage.models import InvestigatorProfile

# Create your models here.

class QueryModel(models.Model):
    email=models.ForeignKey(InvestigatorProfile,on_delete=models.CASCADE)
    description=models.CharField(max_length=1000)
    status=models.CharField(max_length=1000)
    doc=models.DateTimeField(auto_now_add=True)
    dou=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email.email