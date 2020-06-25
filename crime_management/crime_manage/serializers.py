from rest_framework import serializers
from crime_manage import models
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from email_service.views import SendMailClass
from images_app.views import InsertImage


class InvestigatorsAdministrativeDetailSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    email=serializers.EmailField(max_length=200)
    class Meta:
        model=models.InvestigatorsAdministrativeDetail
        fields=['id','salary','achivements','position','email']

    def create(self,validated_data):
        email_id=validated_data.pop('email')
        try:
            investigator_obj=models.InvestigatorProfile.objects.get(email=email_id)
        except models.InvestigatorProfile.DoesNotExist:
            invst_obj=models.InvestigatorProfile(email="1@gmail.com")
            obj=models.InvestigatorsAdministrativeDetail(email=invst_obj)
            return obj
        try:
            admin_obj=models.InvestigatorsAdministrativeDetail.objects.get(email=investigator_obj)
            invst_obj=models.InvestigatorProfile(email="2@gmail.com")
            obj=models.InvestigatorsAdministrativeDetail(email=invst_obj)
            return obj
        except models.InvestigatorsAdministrativeDetail.DoesNotExist:
            admin_obj1=models.InvestigatorsAdministrativeDetail.objects.create(achivements=validated_data["achivements"],salary=validated_data['salary'],position=validated_data['position'],email=investigator_obj)  
            return admin_obj1
        
            

     
        
    def update(self,instance,validated_data):
        email_id=validated_data.pop('email')
        print(validated_data)
        try:
            investigator_obj=models.InvestigatorProfile.objects.get(email=email_id)
        except models.InvestigatorProfile.DoesNotExist:
            invst_obj=models.InvestigatorProfile(email="1@gmail.com")
            obj=models.InvestigatorsAdministrativeDetail(email=invst_obj)
            return obj
        email=investigator_obj
        instance.email=email
        instance.id=validated_data.get("id",instance.id)
        instance.position=validated_data.get("position",instance.position)
        instance.salary=validated_data.get("salary",instance.salary)
        instance.achivements=validated_data.get("achivements",instance.achivements)
        instance.save()
        return instance


        

    






class InvestigatorAddressSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model=models.InvestigatorAddress
        fields=['resident_id','id','location','city','state','zip_code','longitude','latitude']
      
        
    def create(self,validated_data):
        inv_obj=models.InvestigatorAddress.objects.create(location=validated_data['location'],resident_id=validated_data['resident_id'],city=validated_data['city'],state=validated_data['state'],zip_code=validated_data['zip_code'],latitude=validated_data['latitude'],longitude=validated_data['longitude'])
        return inv_obj


    def update(self,instance,validated_data):
        instance.id=validated_data.get("id",instance.id)
        instance.resident_id=validated_data.get("resident_id",instance.resident_id)
        instance.location=validated_data.get("location",instance.location)
        instance.city=validated_data.get("city",instance.city)
        instance.state=validated_data.get("state",instance.state)
        instance.zip_code=validated_data.get("zip_code",instance.zip_code)
        instance.latitude=validated_data.get('latitude',instance.latitude)
        instance.longitude=validated_data.get('longitude',instance.longitude)
        instance.save()
        return instance
                   
    
class InvestigatorDetailSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    profile_image=serializers.CharField(max_length=2000000000000)
    is_superuser=serializers.BooleanField(required=False)
    is_staff=serializers.BooleanField(required=False)
    is_active=serializers.BooleanField(required=False)
    class Meta:
        model=models.InvestigatorProfile
        fields=['id','first_name','last_name','email','dob','phone_no','gender','password','adhaar_no','is_superuser','is_active',"is_staff","profile_image"]


    def create(self,validated_data):
        send_email_to=validated_data['email']
        print(send_email_to+" ffffff1")
        try:
            print(send_email_to+" ffffff2")
            invst_obj=models.InvestigatorProfile.objects.get(email=send_email_to)
            print(send_email_to+" ffffff3")
            obj=models.InvestigatorProfile(email="userExists@gmail.com")
            return obj
        except models.InvestigatorProfile.DoesNotExist:
            send_email=SendMailClass()
            email_verification_token=send_email.generate_random_string()
            result=send_email.send_email_for_verification(send_email_to,email_verification_token)
            if (result):
                image_data=validated_data["profile_image"]
                i=InsertImage()
                image_name_string=i.insert_image("investigator_profile_pictures",image_data)
                investigator_obj=models.InvestigatorProfile.objects.create_user(
                profile_image=image_name_string,
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                email=validated_data["email"],
                dob=validated_data["dob"],
                adhaar_no=validated_data["adhaar_no"],
                phone_no=validated_data["phone_no"],
                gender=validated_data["gender"],
                password=validated_data["password"],
                status=False,email_verification_token=email_verification_token)
                return investigator_obj
            dummy_obj=models.InvestigatorProfile(email="noInternet@gmail.com")
            return dummy_obj
        
        
        
        
            
            
                

    def update(self,instance,validated_data):

        #obj=models.InvestigatorProfile.objects.get(id=validated_data["id"])
        
        #print(instance.email)
        #print(validated_data.get("email"))
        #if instance.email!=validated_data["email"]:
            #try:
                #print("jerr")
                #invst_obj=models.InvestigatorProfile.objects.get(email=validated_data["email"])
                #obj=models.InvestigatorProfile(email="userExists@gmail.com")
                #return obj
            #except models.InvestigatorProfile.DoesNotExist:
                #pass
        image_name_string=validated_data["profile_image"];
        print(str(len(image_name_string)))
        print("out if")
        if len(image_name_string)>25:
            print("in if")
            i=InsertImage()
            image_name_string=i.insert_image("investigator_profile_pictures",image_name_string)
        instance.profile_image=image_name_string
        instance.id=validated_data.get('id',instance.id)
        instance.first_name=validated_data.get("first_name",instance.first_name)
        instance.last_name=validated_data.get("last_name",instance.last_name)
        instance.email=validated_data.get("email",instance.email)
        instance.dob=validated_data.get("dob",instance.dob)
        instance.phone_no=validated_data.get("phone_no",instance.phone_no)
        instance.gender=validated_data.get("gender",instance.gender)
        instance.password=validated_data.get("password",instance.password)
        instance.is_superuser=validated_data.get("is_superuser",instance.is_superuser)
        instance.is_staff=validated_data.get("is_staff",instance.is_staff)
        instance.is_active=validated_data.get("is_active",instance.is_active)
        instance.adhaar_no=validated_data.get("adhaar_no",instance.adhaar_no)
        instance.save()
        return instance
        


 