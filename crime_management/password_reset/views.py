from django.shortcuts import render
from crime_manage.models import InvestigatorProfile
from password_reset.serializers import PasswordRestSerializer,PasswordOTPVerificationSerializer,PasswordUpdateSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



class PasswordResetAPI(APIView):

    def post(self,request,format=None):
        serializer= PasswordRestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            if serializer.data['email']=="1":
                return Response({"message":"you are not a Authorized user","flag":False},status=status.HTTP_200_OK)

            if serializer.data['email']=="2":
                return Response({'message':"Check Your Email for Verification Code","flag":True},status=status.HTTP_200_OK)

            if serializer.data['email']=="3":
                return Response({"message":"Error while generating Verfication Code","flag":False},status=status.HTTP_200_OK)

        return Response({"message":False},status=status.HTTP_200_OK)

        
class PasswordOTPVerificationAPI(APIView):

    def post(self,request,format=False):
        serializer=PasswordOTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if(serializer.data['email']=="1"):
                return Response({"message":"Successfully OTP Verified","flag":True},status=status.HTTP_200_OK)
            if(serializer.data['email']=="0"):
                return Response({"message":"Invalid OTP","flag":False},status=status.HTTP_200_OK)
        return Response({"message":"Validation Error","flag":False},status=status.HTTP_200_OK)



class PasswordUpdateAPI(APIView):

    def post(self,request,format=None):
        serializer=PasswordUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if(serializer.data['email']=="1"):
                return Response({"message":"Successfully Updated","flag":True},status=status.HTTP_200_OK)
            if(serializer.data['email']=="0"):
                return Response({"message":"Invalid Email ID","flag":False},status=status.HTTP_200_OK)
        return Response({"message":"Validation Error","flag":False},status=status.HTTP_200_OK)

      
       

