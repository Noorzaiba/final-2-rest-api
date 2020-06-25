from django.db import models
from cases_information.models import CrimeDetail









class CriminalDetail(models.Model):
    profile_image=models.CharField(max_length=300,blank=True)
    first_name=models.CharField(max_length=200,default='unknown')
    last_name=models.CharField(max_length=200,null=True,blank=True,default='unknown')
    age=models.PositiveIntegerField(null=True,blank=True,default=0)
    phone_no=models.PositiveIntegerField(null=True,blank=True,default=0)
    email=models.EmailField(max_length=200,null=True,blank=True,default='unknown@gmail.com')
    gender=models.CharField(max_length=8,default="unknown")
    doc=models.DateTimeField(auto_now_add=True)
    dou=models.DateTimeField(auto_now=True)
    crime_id=models.ForeignKey(CrimeDetail,on_delete=models.CASCADE)
    adhaar_no=models.PositiveIntegerField(null=True,blank=True,default=0)
    occupation=models.CharField(max_length=200,null=True,blank=True,default='unknown')
    salary=models.PositiveIntegerField(null=True,blank=True,default=0)
    remarks=models.CharField(max_length=500,default="unknown",null=True,blank=True)
    





    @property
    def address(self):
        address=self.criminaldetailaddress_set.all()
        return address
    
        


    def __str__(self):
        return self.first_name



class VictimDetail(models.Model):
    profile_image=models.CharField(max_length=300,blank=True)
    first_name=models.CharField(max_length=200,default='unknown')
    last_name=models.CharField(max_length=200,null=True,blank=True,default='unknown')
    age=models.PositiveIntegerField(null=True,blank=True,default=0)
    phone_no=models.PositiveIntegerField(null=True,blank=True,default=0)
    email=models.EmailField(max_length=200,null=True,blank=True,default="unknown@gmail.com")
    gender=models.CharField(max_length=8,default='unknown')
    doc=models.DateTimeField(auto_now_add=True)
    dou=models.DateTimeField(auto_now=True)
    crime_id=models.ForeignKey(CrimeDetail,on_delete=models.CASCADE)
    adhaar_no=models.PositiveIntegerField(null=True,blank=True,default=0)
    occupation=models.CharField(max_length=200,null=True,blank=True,default="unknown")
    salary=models.PositiveIntegerField(null=True,blank=True,default=0)
    remarks=models.CharField(max_length=500,default="unknown",null=True,blank=True)
    






    @property
    def address(self):
        address=self.victimdetailaddress_set.all()
        return address
    
        


    def __str__(self):
        return self.first_name


 
  


class CriminalDetailAddress(models.Model):
    resident_id=models.ForeignKey(CriminalDetail,on_delete=models.CASCADE,default=0)
    location=models.CharField(max_length=300,default='unknown')
    city=models.CharField(max_length=200,default='unknown')
    state=models.CharField(max_length=200,default='unknown')
    zip_code=models.PositiveIntegerField(default=0)
    longitude=models.DecimalField(decimal_places=20,max_digits=300,default=0)
    latitude=models.DecimalField(decimal_places=20,max_digits=300,default=0)
    def __str__(self):
        return self.location




class VictimDetailAddress(models.Model):
    resident_id=models.ForeignKey(VictimDetail,on_delete=models.CASCADE,default=0)
    location=models.CharField(max_length=300,default='unknown')
    city=models.CharField(max_length=200,default='unknown')
    state=models.CharField(max_length=200,default='unknown')
    zip_code=models.PositiveIntegerField(default=0)
    longitude=models.DecimalField(decimal_places=20,max_digits=300,default=0)
    latitude=models.DecimalField(decimal_places=20,max_digits=300,default=0)
    
    def __str__(self):
        return self.location


