from rest_framework import serializers
from django.contrib.auth import authenticate
from django.core.exceptions import  ValidationError
from crime_manage.models import InvestigatorProfile
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password



   

class InvestigatorLoginSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=50)
    email=serializers.CharField(max_length=100)
    id=serializers.CharField(required=False)
    first_name=serializers.CharField(required=False)
    last_name=serializers.CharField(required=False)
    is_superuser=serializers.BooleanField(required=False)
    is_staff=serializers.BooleanField(required=False)
  

    def create(self,validated_data):
        password=validated_data['password']
        email=validated_data['email']
        print(email)
        print(password)
      
        try:
            user_obj=InvestigatorProfile.objects.get(email=email)
            status=user_obj.status
            active=user_obj.is_active
            if status==False:
                obj=InvestigatorProfile(email="3")
                print("1")
                return obj
            if active==False:
                obj=InvestigatorProfile(email="4")
                print("66")
                return obj
            encrypted_password=user_obj.password
            flag=check_password(password,encrypted_password)
            if flag:
                token,created=Token.objects.get_or_create(user=user_obj)
                
                print("12")
                obj=InvestigatorProfile(email=user_obj.email,id=user_obj.id,first_name=user_obj.first_name,last_name=token,is_superuser=user_obj.is_superuser,is_staff=user_obj.is_staff)
                print(user_obj.id)
                return obj
            else:
                print("13")
                obj=InvestigatorProfile(email="1")
                return obj
        except InvestigatorProfile.DoesNotExist:
            obj=InvestigatorProfile(email="2")
            print("14")
            return obj


 