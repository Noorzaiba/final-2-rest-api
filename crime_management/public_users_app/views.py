from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from public_users_app import models
from public_users_app import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from public_users_app.permissions import CustomPermissionCheck
from accounts.authentication import CustomAuthentication,CustomTokenAuthentication,CustomAuthenticationForPublicUsersAndInvestigators
# Create your views here.
import datetime
from images_app.views import DeleteImage



class PublicUserLoginAPI(APIView):

            
    def post(self,request,format=None):
        serializer=serializers.PublicUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if serializer.data["email_id"]=="1":
                content={"flag":False,"message":"Invalid Credentials Provided"}
                print(content)
                return Response(content,status=status.HTTP_200_OK)  
            elif serializer.data["email_id"]=="2":
                content={"flag":False,"message":"Invalid Email ID"}
                return Response(content,status=status.HTTP_200_OK)  
            elif serializer.data["email_id"]=="3":
                content={"flag":False,"message":"Email Validation Pending Please Refer your email to finish the process"}
                return Response(content,status=status.HTTP_200_OK)
            else:
                content={"user":serializer.data,"flag":True,"message":"Login Successfully"}
                return Response(content,status=status.HTTP_200_OK)  
        content={"user":serializer.errors,"flag":False,"message":"Validation Error"}
        print(content)
        return Response(content,status=status.HTTP_200_OK)
 
    





def emailVerification(request,email_verification_token):
    print(email_verification_token+ "in index")
    if email_verification_token:
        obj=get_object_or_404(models.PublicUser,email_verification_token=email_verification_token)
        print(obj.status)
        obj.status=True
        obj.email_verification_token="null"
        obj.save()
        print(obj.status)
        return render(request,"public_users_app/index.html",{"email_verification_token":email_verification_token,"success":'Email successfully verified'})
    return render(request,"public_users_app/index.html",{"email_verification_token":email_verification_token,"success":"Unsucess at Email verification plz register agian"})







class PublicUserListAPI(APIView):

    def get(self,request,format=None):
        public_users=models.PublicUser.objects.all()
        serializer=serializers.PublicUserSerializer(public_users,many=True)
        content={"flag":True,"serialized_data":serializer.data}
        print(content)
        return Response(content,status=status.HTTP_200_OK)



            
    def post(self,request,format=None):
        serializer=serializers.PublicUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,"serialized_data":[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)  
        errors_in_process=serializer.errors['email_id']
        print(errors_in_process)
        s=errors_in_process[0]
        print(s)
        content={"flag":False,"serialized_data":[{'email_id':s}]}
        return Response(content,status=status.HTTP_200_OK)
 
    




class PublicUserAddressListAPI(APIView):
    def get(self,request,format=None):
        public_users_address=models.PublicUserAddress.objects.all()
        serializer=serializers.PublicUserAddressSerializer(public_users_address,many=True)
        content={"flag":True,"serialized_data":serializer.data}
        return Response(content,status=status.HTTP_200_OK)



            
    def post(self,request,format=None):
        serializer=serializers.PublicUserAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,"serialized_data":[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)  
        content={"flag":False,"serialized_data":[serializer.errors]}
        return Response(content,status=status.HTTP_200_OK)
 


class PublicUserDetailAPI(APIView):
    lookup_field='email_id'
    authentication_classes=(CustomAuthenticationForPublicUsersAndInvestigators,)
    permission_classes=(IsAuthenticated,)
    def get_object(self,email_id):
        try:
            return models.PublicUser.objects.get(email_id=email_id)
        except models.PublicUser.DoesNotExist:
            raise Http404

    def get(self,request,email_id,format=None):
        public_user_obj=self.get_object(email_id)
        print("sentered")
        serializer=serializers.PublicUserSerializer(public_user_obj)
        content={"flag":True,"serialized_data":[serializer.data]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def put(self,request,email_id,format=None):
        public_user_obj=self.get_object(email_id)
        serializer=serializers.PublicUserSerializer(public_user_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        errors_in_process=serializer.errors['email_id']
        print(errors_in_process)
        s=errors_in_process[0]
        print(s)
        content={"flag":False,"serialized_data":[{'email_id':s}]}
        print(content)
        print(serializer.errors)
        return Response(content,status=status.HTTP_200_OK)

    def delete(self,request,email_id,format=None):
        public_user_obj=self.get_object(email_id)
        image_name=public_user_obj.profile_image
        public_user_obj.delete()
        print("here is image name")
        print(image_name)
        d=DeleteImage()
        z=d.delete_image("public_user_profile_pictures",image_name)
        print(z)
        content={"flag":True}
        return Response(content,status=status.HTTP_200_OK)



class PublicUserAddressDetailAPI(APIView):
    lookup_field='resident_id'
    #authentication_classes=(CustomAuthenticationForPublicUsersAndInvestigators,)
    #permission_classes=(IsAuthenticated,)
    def get_object(self,resident_id):
        try:
            return models.PublicUserAddress.objects.get(resident_id=resident_id)
        except models.PublicUserAddress.DoesNotExist:
            return False


    def get(self,request,resident_id,format=None):
        public_user_address_obj=self.get_object(resident_id)
        if public_user_address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)

        print("sentered")
        serializer=serializers.PublicUserAddressSerializer(public_user_address_obj)
        content={"flag":True,"serialized_data":[serializer.data]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def put(self,request,resident_id,format=None):
        public_user_address_obj=self.get_object(resident_id)
        if public_user_address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        print(request.data)
        serializer=serializers.PublicUserAddressSerializer(public_user_address_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def delete(self,request,resident_id,format=None):
        public_user_address_obj=self.get_object(resident_id)
        if public_user_address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        public_user_address_obj.delete()
        content={"flag":True}
        return Response(content,status=status.HTTP_200_OK)




class ImageAPI(APIView):
    def get(self,request,format=None):
        public_users_address=models.ImageDemo.objects.all()
        serializer=serializers.ImageDemoSerializer(public_users_address,many=True)
        content={"flag":True,"serialized_data":serializer.data}
        return Response(serializer.data,status=status.HTTP_200_OK)



            
    def post(self,request,format=None):
        serializer=serializers.ImageDemoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({},status=status.HTTP_200_OK)  
        return Response({},status=status.HTTP_200_OK)  
    