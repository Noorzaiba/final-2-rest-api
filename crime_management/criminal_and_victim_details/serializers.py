from rest_framework import serializers
from criminal_and_victim_details.models import VictimDetailAddress,CriminalDetailAddress,CriminalDetail,VictimDetail
from django.shortcuts import get_object_or_404
from cases_information.models import CrimeDetail
from images_app.views import InsertImage






class VictimDetailAddressSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model=VictimDetailAddress
        fields=['resident_id','id','location','city','state','zip_code','longitude','latitude']
       
    def create(self,validated_data):
        obj=VictimDetailAddress.objects.create(location=validated_data['location'],resident_id=validated_data['resident_id'],city=validated_data['city'],state=validated_data['state'],zip_code=validated_data['zip_code'],latitude=validated_data['latitude'],longitude=validated_data['longitude'])
        return obj

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
                   

class CriminalDetailAddressSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model=CriminalDetailAddress
        fields=['resident_id','id','location','city','state','zip_code','longitude','latitude']
       

    def create(self,validated_data):
        obj=CriminalDetailAddress.objects.create(location=validated_data['location'],resident_id=validated_data['resident_id'],city=validated_data['city'],state=validated_data['state'],zip_code=validated_data['zip_code'],latitude=validated_data['latitude'],longitude=validated_data['longitude'])
        return obj

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



class VictimDetailSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    crime_id=serializers.CharField(max_length=20)
    profile_image=serializers.CharField(max_length=2000000000000)

    class Meta:
        model=VictimDetail
        fields=['id',"profile_image",'first_name','last_name','email','age','doc','dou','phone_no','gender','adhaar_no','occupation','remarks','salary','crime_id']


    def create(self,validated_data):
        crime_id=validated_data["crime_id"]
        try:
            crime_obj=CrimeDetail.objects.get(id=crime_id)
        except CrimeDetail.DoesNotExist:
            dummy_obj=VictimDetail(email="Invalid_Crime_id")
            return dummy_obj    
       
        image_name_string=validated_data["profile_image"]
        print(str(len(image_name_string)))
        print("out if")
        if len(image_name_string)>25:
            print("in if")
            i=InsertImage()
            image_name_string=i.insert_image("victim_criminal_profile_pictures",image_name_string)
        
        
        victim_obj=VictimDetail.objects.create(
                first_name=validated_data["first_name"],
                profile_image=image_name_string,
                last_name=validated_data["last_name"],
                email=validated_data["email"],
                age=validated_data["age"],
                adhaar_no=validated_data["adhaar_no"],
                phone_no=validated_data["phone_no"],
                gender=validated_data["gender"],
                crime_id=crime_obj,
                occupation=validated_data["occupation"],
                remarks=validated_data["remarks"],
                salary=validated_data["salary"])
        return victim_obj
        
       
       


    def update(self,instance,validated_data):
        crime_id=validated_data["crime_id"]
        try:
            crime_obj=CrimeDetail.objects.get(id=crime_id)
        except CrimeDetail.DoesNotExist:
            dummy_obj=VictimDetail(email="Invalid_Crime_id")
            return dummy_obj   
        image_name_string=validated_data["profile_image"];
        print(str(len(image_name_string)))
        print("out if")
        if len(image_name_string)>25:
            print("in if")
            i=InsertImage()
            image_name_string=i.insert_image("victim_criminal_profile_pictures",image_name_string)
        instance.profile_image=image_name_string 
        instance.id=validated_data.get('id',instance.id)
        instance.first_name=validated_data.get("first_name",instance.first_name)
        instance.last_name=validated_data.get("last_name",instance.last_name)
        instance.email=validated_data.get("email",instance.email)
        instance.age=validated_data.get("age",instance.age)
        instance.phone_no=validated_data.get("phone_no",instance.phone_no)
        instance.gender=validated_data.get("gender",instance.gender)
        instance.remarks=validated_data.get("remarks",instance.remarks)
        instance.crime_id=crime_obj
        instance.occupation=validated_data.get("occupation",instance.occupation)
        instance.salary=validated_data.get("salary",instance.salary)
        instance.adhaar_no=validated_data.get("adhaar_no",instance.adhaar_no)
        instance.save()
        return instance










class CriminalDetailSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    crime_id=serializers.CharField(max_length=20)
    profile_image=serializers.CharField(max_length=2000000000000)

    class Meta:
        model=CriminalDetail
        fields=['id',"profile_image",'first_name','last_name','email','age','phone_no','gender','doc','dou','remarks','adhaar_no','occupation','salary','crime_id']
       
    def create(self,validated_data):
        crime_id=validated_data["crime_id"]
        try:
            crime_obj=CrimeDetail.objects.get(id=crime_id)
        except CrimeDetail.DoesNotExist:
            dummy_obj=CriminalDetail(email="Invalid_Crime_id")
            return dummy_obj    
        image_name_string=validated_data["profile_image"]
        print(str(len(image_name_string)))
        print("out if")
        if len(image_name_string)>25:
            print("in if")
            i=InsertImage()
            image_name_string=i.insert_image("victim_criminal_profile_pictures",image_name_string)
        obj=CriminalDetail.objects.create(
                first_name=validated_data["first_name"],
                profile_image=image_name_string,
                last_name=validated_data["last_name"],
                email=validated_data["email"],
                age=validated_data["age"],
                adhaar_no=validated_data["adhaar_no"],
                phone_no=validated_data["phone_no"],
                gender=validated_data["gender"],
                crime_id=crime_obj,
                occupation=validated_data["occupation"],
                remarks=validated_data["remarks"],
                salary=validated_data["salary"])
        return obj
        
       

    def update(self,instance,validated_data):
        try:
            crime_id=validated_data.get("crime_id",instance.crime_id)
            crime_obj=CrimeDetail.objects.get(id=crime_id)
        except CrimeDetail.DoesNotExist:
            dummy_obj=CriminalDetail(email="Invalid_Crime_id")
            return dummy_obj   
        image_name_string=validated_data["profile_image"]
        print("image data")
        print(str(len(image_name_string)))
        print("out if")
        if len(image_name_string)>25:
            print("in if")
            i=InsertImage()
            image_name_string=i.insert_image("victim_criminal_profile_pictures",image_name_string)
        instance.profile_image=image_name_string
        instance.id=validated_data.get('id',instance.id)
        instance.first_name=validated_data.get("first_name",instance.first_name)
        instance.last_name=validated_data.get("last_name",instance.last_name)
        instance.email=validated_data.get("email",instance.email)
        instance.age=validated_data.get("age",instance.age)
        instance.phone_no=validated_data.get("phone_no",instance.phone_no)
        instance.gender=validated_data.get("gender",instance.gender)
        instance.remarks=validated_data.get("remarks",instance.remarks)
        instance.crime_id=crime_obj
        instance.occupation=validated_data.get("occupation",instance.occupation)
        instance.salary=validated_data.get("salary",instance.salary)
        instance.adhaar_no=validated_data.get("adhaar_no",instance.adhaar_no)
        instance.save()
        return instance

