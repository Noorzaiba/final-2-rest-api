from django.db import models
from django.contrib.auth.hashers import make_password



class ImageDemo(models.Model):
    profile_image=models.ImageField(upload_to="publicuser_profile_images",blank=True)



class PublicUser(models.Model):
    profile_image=models.CharField(max_length=300,blank=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email_id=models.EmailField(max_length=300,unique=True)
    dob=models.DateField(blank=True,null=True)
    phone_no=models.IntegerField()
    gender=models.CharField(max_length=7)
    password=models.CharField(max_length=1000)
    adhaar_no=models.PositiveIntegerField(null=True)
    doc=models.DateTimeField(auto_now_add=True)
    dou=models.DateTimeField(auto_now=True)
    email_verification_token=models.CharField(max_length=1000,blank=True,default=True)
    status=models.BooleanField(blank=True,default=False)

    def is_authenticated(email):
        obj=PublicUser.objects.get(email_id=email)
        if obj:
            return True
        else:
            return False



    '''def save(self,*args,**kwargs):
        self.password=make_password(self.password)
        super(PublicUser,self).save(*args,**kwargs)'''


    def __str__(self):
        return self.email_id

    @property
    def address(self):
        address=self.publicuseraddress_set.all()
        return address
    




class PublicUserAddress(models.Model):
    resident_id=models.ForeignKey(PublicUser,on_delete=models.CASCADE)
    location=models.CharField(max_length=300)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zip_code=models.PositiveIntegerField()
    longitude=models.DecimalField(max_digits=300,decimal_places=15,default=0)
    latitude=models.DecimalField(max_digits=300,decimal_places=15,default=0)
    def __str__(self):
        return self.location
        
