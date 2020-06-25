from django.db import models
from public_users_app.models import PublicUser

class CrimeReported(models.Model):
    TYPE_OF_CRIME_CHOICES=[('Robbery','Robbery'),('Murder',"Murder"),('Acid Throwing','Acid Throwing'),('Ragging',"Ragging"),('Property',"Property "),('Others',"Others"),('Smuggling',"Smuggling"),('Vandalism',"Vandalism"),('Torture',"Torture")]
    type_of_crime=models.CharField(max_length=300,null=True,blank=True,choices=TYPE_OF_CRIME_CHOICES)
    description=models.CharField(max_length=400)
    date=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    doc=models.DateTimeField(auto_now_add=True)
    dou=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=200,default='null')
    user=models.ForeignKey(PublicUser,on_delete=models.CASCADE)
    final_submit=models.BooleanField(default=False)
    remarks=models.CharField(default="null",max_length=1000)


    def __str__(self):
        return str(self.id)
    


    @property
    def address(self):
        address=self.crimereportedlocation_set.all()
        return address


class CrimeReportedLocation(models.Model):
    resident_id=models.ForeignKey(CrimeReported,on_delete=models.CASCADE)
    location=models.CharField(max_length=300)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zip_code=models.PositiveIntegerField()
    longitude=models.DecimalField(decimal_places=15,max_digits=300,default=0)
    latitude=models.DecimalField(decimal_places=15,max_digits=300,default=0)
    
    def __str__(self):
        return self.location
        

