from rest_framework import serializers
from public_users_app import models
from django.shortcuts import get_object_or_404
from email_service.views import SendMailClass
from django.contrib.auth.hashers import make_password,check_password
from images_app.views import InsertImage

class PublicUserLoginSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=50)
    email_id=serializers.CharField(max_length=100)
    id=serializers.IntegerField(required=False)
    first_name=serializers.CharField(required=False)
  

    def create(self,validated_data):
        password=validated_data['password']
        email_id=validated_data['email_id']

        print(password)
      
        try:
            public_user_obj=models.PublicUser.objects.get(email_id=email_id)
            status=public_user_obj.status
            if status==False:
                obj=models.PublicUser(email_id="3")
                return obj

            encrypted_password=public_user_obj.password
            flag=check_password(password,encrypted_password)
            if flag:
                obj=models.PublicUser(email_id=public_user_obj.email_id,id=public_user_obj.id,first_name=public_user_obj.first_name)
                return obj
            else:
                obj=models.PublicUser(email_id="1")
                return obj
        except models.PublicUser.DoesNotExist:
            obj=models.PublicUser(email_id="2")
            return obj




class PublicUserAddressSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    
    class Meta:
        model=models.PublicUserAddress
        fields=['resident_id','id','location','city','state','zip_code','latitude','longitude']
        

    def create(self,validated_data):
        crime_address_obj=models.PublicUserAddress.objects.create(location=validated_data['location'],resident_id=validated_data['resident_id'],city=validated_data['city'],state=validated_data['state'],zip_code=validated_data['zip_code'],latitude=validated_data['latitude'],longitude=validated_data['longitude'])
        return crime_address_obj


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
                   
    


class PublicUserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(required=False)
    id=serializers.IntegerField(required=False)
    profile_image=serializers.CharField(max_length=2000000000000)


    class Meta:
        model=models.PublicUser
        fields=['email_id',"profile_image",'id','first_name','last_name','dob','phone_no','gender','adhaar_no','password',"profile_image"]



    def create(self,validated_data):
        send_email_to=validated_data['email_id']
        password=make_password(validated_data.pop('password'))
        
        try:
            public_user_obj=models.PublicUser.objects.get(email_id=send_email_to)
            obj=models.PublicUser(email_id="userExists@gmail.com")
            return obj
        except models.PublicUser.DoesNotExist:
            send_email=SendMailClass()
            email_verification_token=send_email.generate_random_string()
            result=send_email.send_email_for_verification_for_public_users(send_email_to,email_verification_token)
            if result:
                image_data=validated_data["profile_image"]
                i=InsertImage()
                image_name_string=i.insert_image("public_user_profile_pictures",image_data)
                public_user_obj=models.PublicUser.objects.create(
                profile_image=image_name_string,
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                email_id=validated_data["email_id"],
                dob=validated_data["dob"],
                adhaar_no=validated_data["adhaar_no"],
                phone_no=validated_data["phone_no"],
                gender=validated_data["gender"],
                password=password,status=False,email_verification_token=email_verification_token)
                return public_user_obj
            dummy_obj=models.PublicUser(email_id="noInternet@gmail.com")
            return dummy_obj


    
               

    def update(self,instance,validated_data):
        image_name_string=validated_data["profile_image"];
        print(str(len(image_name_string)))
        print("out if")
        if len(image_name_string)>25:
            print("in if")
            i=InsertImage()
            image_name_string=i.insert_image("public_user_profile_pictures",image_name_string)
        instance.profile_image=image_name_string
        instance.id=validated_data.get("id",instance.id)
        instance.first_name=validated_data.get("first_name",instance.first_name)
        instance.last_name=validated_data.get("last_name",instance.last_name)
        instance.email_id=validated_data.get("email_id",instance.email_id)
        instance.dob=validated_data.get("dob",instance.dob)
        instance.gender=validated_data.get("gender",instance.gender)
        instance.password=validated_data.get("password",instance.password)
        instance.adhaar_no=validated_data.get("adhaar_no",instance.adhaar_no)
        instance.phone_no=validated_data.get("phone_no",instance.phone_no)
        instance.save()
        return instance




class ImageDemoSerializer(serializers.Serializer):
   
    image1=serializers.CharField(max_length=100000000000000000000000)
   
        
    def create(self,validated_data):   
        image_data=validated_data["image1"]
       
        image_data_in_bytes=bytes(image_data,"utf-8")
        image_form=base64.decodestring(image_data_in_bytes)
        image=Image.open(BytesIO(image_form))
        now=str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-"))
        file_name="/"+now+str(get_random_string(length=7,allowed_chars='123456789'))+".jpg"
        print(file_name)
        image.save(settings.MEDIA_ROOT+file_name)
        ob1="abc"
        ob1.encode("ASCII")
        return ob1
        
       
      


  
