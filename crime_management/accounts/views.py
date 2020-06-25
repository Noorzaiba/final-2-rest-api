from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import InvestigatorLoginSerializer
from crime_manage.models import InvestigatorProfile
from django.contrib.auth import login as django_login,logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework import status






class InvestigatorLoginAPI(APIView):
    def post(self,request,format=None):
        print(request.data)
        serializer=InvestigatorLoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if serializer.data["email"]=="1":
                content={"flag":False,"message":"Invalid Credentials Provided"}
                print(content)
                return Response(content,status=status.HTTP_200_OK)  
            elif serializer.data["email"]=="2":
                content={"flag":False,"message":"Invalid Email ID"}
                print(content)
                return Response(content,status=status.HTTP_200_OK)  
            elif serializer.data["email"]=="3":
                content={"flag":False,"message":"Email Validation Pending Please Refer your email to finish the process"}
                print(content)
                return Response(content,status=status.HTTP_200_OK)
            elif serializer.data["email"]=="4":
                content={"flag":False,"message":"Your Account has been deactivated"}
                print(content)
                return Response(content,status=status.HTTP_200_OK)
            else:
                content={"user":serializer.data,"flag":True,"message":"Login Successfully"}
                print(content)
                return Response(content,status=status.HTTP_200_OK)  
        content={"user":serializer.errors,"flag":False,"message":"Validation Error"}
        print(content)
        return Response(content,status=status.HTTP_200_OK)
 


        

     
  
