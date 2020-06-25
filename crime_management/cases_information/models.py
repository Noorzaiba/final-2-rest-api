from django.db import models
from crime_manage.models import InvestigatorProfile
from datetime import date


# Create your models here.


class CrimeDetail(models.Model):
    TYPE_OF_CRIME_CHOICES=[('Robbery','Robbery'),('Murder',"Murder"),('Acid Throwing','Acid Throwing'),('Ragging',"Ragging"),('Property',"Property "),('Others',"Others"),('Smuggling',"Smuggling"),('Vandalism',"Vandalism"),('Torture',"Torture")]
    type_of_crime=models.CharField(max_length=300,null=True,blank=True,choices=TYPE_OF_CRIME_CHOICES)
    description=models.CharField(max_length=400)
    date=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    doc=models.DateTimeField(auto_now_add=True)
    dou=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=200,default='null')
    investigator_id=models.ForeignKey(InvestigatorProfile,on_delete=models.CASCADE)
   

    def __str__(self):
        return str(self.id)




  
        
class CrimeLocationDetail(models.Model):
    resident_id=models.ForeignKey(CrimeDetail,on_delete=models.CASCADE,default=0)
    location=models.CharField(max_length=300,default="null")
    city=models.CharField(max_length=200,default="null")
    state=models.CharField(max_length=200,default="null")
    zip_code=models.PositiveIntegerField(default=0)
    longitude=models.DecimalField(decimal_places=20,max_digits=300,default=0)
    latitude=models.DecimalField(decimal_places=20,max_digits=300,default=0)

    def __str__(self):
        return self.location


class CrimeLiveUpdation(models.Model):
    crime_id=models.ForeignKey(CrimeDetail,on_delete=models.CASCADE)
    comments=models.CharField(max_length=300,null=True,blank=True)
    doc=models.DateTimeField(auto_now_add=True)
    dou=models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.location
  
