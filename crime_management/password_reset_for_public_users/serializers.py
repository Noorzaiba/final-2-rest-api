

from password_reset_for_public_users import models
from django.contrib.auth.hashers import make_password
from public_users_app.models import PublicUser
from email_service import views
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.core.exceptions import  ValidationError




class PasswordGetEmailSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=200)


class PasswordRestSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=200)
   
    
    def create(self,validated_data):
        email=validated_data['email']
        try:
            public_user_obj=PublicUser.objects.get(email_id=email)
            status=public_user_obj.status
            if status==False:
                return {"email":"4"}
        except PublicUser.DoesNotExist:
            return {"email":"1"}
        send_email=views.SendMailClass()
        password_otp=send_email.generate_random_number()
        result=send_email.send_email_for_password_reset(public_user_obj.email_id,password_otp)
        if result:
            obj=models.PasswordRestForPublicUsers.objects.create(otp=password_otp,email=public_user_obj.email_id,status=False)
            return {'email':"2"}
        return {"email":"3"}







class PasswordOTPVerificationSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=200)
    otp=serializers.CharField(max_length=8)
    
    def create(self,validated_data):
        otp=validated_data['otp']
        email=validated_data['email']
        try:
           password_rest_obj=models.PasswordRestForPublicUsers.objects.get(email=email,otp=otp)
           password_rest_obj.status=True
           password_rest_obj.otp="null"
           password_rest_obj.save()
           return {"email":'1',"otp":"1"}
        except models.PasswordRestForPublicUsers.DoesNotExist:
            return {"email":'0',"otp":"0"}
       

 


class PasswordUpdateSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=200)
    email=serializers.CharField(max_length=300)

    def create(self,validated_data):
        passsword=validated_data['password']
        email=validated_data['email']
        try:
            public_user_obj=PublicUser.objects.get(email_id=email)
            public_user_obj.password=make_password(passsword)
            public_user_obj.save()
            return{"email":"1","password":"1"}
        except PublicUser.DoesNotExist:
            return{"email":"0","password":"1"}
        
