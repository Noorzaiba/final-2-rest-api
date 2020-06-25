from django.db import models
from django.contrib.auth.models import PermissionsMixin,BaseUserManager,AbstractBaseUser

# Create your models here.



class InvestigatorProfileManager(BaseUserManager):

    def create_user(self,first_name,last_name,email,dob,phone_no,gender,password,adhaar_no,email_verification_token,status,profile_image):

        if not email:
            raise ValueError("User must have an email address")
        email=self.normalize_email(email)
        user=self.model(email=email,profile_image=profile_image,first_name=first_name,last_name=last_name,phone_no=phone_no,
        gender=gender,dob=dob,password=password,adhaar_no=adhaar_no,email_verification_token=email_verification_token,status=status)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,first_name,last_name,dob,phone_no,gender,password,adhaar_no,email_verification_token,status,profile_image):
        user=self.create_user(first_name,last_name,email,dob,phone_no,gender,password,adhaar_no,email_verification_token,status,profile_image)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user






class InvestigatorProfile(AbstractBaseUser,PermissionsMixin):
    profile_image=models.CharField(max_length=300,blank=True)
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=300,unique=True)
    phone_no=models.IntegerField(null=True)
    gender=models.CharField(max_length=7,null=True)
    dob=models.DateField(null=True)
    password=models.CharField(null=True,max_length=1000)
    adhaar_no=models.PositiveIntegerField(null=True)
    doc=models.DateTimeField(auto_now_add=True,null=True)
    dou=models.DateTimeField(auto_now=True,null=True)
    is_active=models.BooleanField(default=True,null=True)
    is_staff=models.BooleanField(default=False)
    email_verification_token=models.CharField(max_length=1000,blank=True,default=True)
    status=models.BooleanField(blank=True,default=False)
  

   
    objects=InvestigatorProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','dob','phone_no','gender','adhaar_no',"email_verification_token","status","profile_image"]

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name



    @property
    def address(self):
        address=self.investigatoraddress_set.all()
        return address
    
        


    def __str__(self):
        return self.email

class InvestigatorAddress(models.Model):
    resident_id=models.ForeignKey(InvestigatorProfile,on_delete=models.CASCADE)
    location=models.CharField(max_length=300)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zip_code=models.PositiveIntegerField()
    longitude=models.DecimalField(decimal_places=20,max_digits=300,default=0)
    latitude=models.DecimalField(decimal_places=20,max_digits=300,default=0)
    
    def __str__(self):
        return self.location



class InvestigatorsAdministrativeDetail(models.Model):
    email=models.ForeignKey(InvestigatorProfile,on_delete=models.CASCADE)
    salary=models.DecimalField(max_digits=300,decimal_places=10,default=00)
    achivements=models.CharField(max_length=300,default="unknown")
    position=models.CharField(max_length=200,default='unknown')
   
    def __str__(self):
        return str(self.id)

