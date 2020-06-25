from django.shortcuts import render
from public_user_contact_us_app.models import QueryModel
from public_user_contact_us_app.serializers import QuerySerializer
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from public_users_app import models
from rest_framework.permissions import IsAuthenticated
from public_users_app.permissions import CustomPermissionCheck
from accounts.authentication import CustomAuthentication,CustomTokenAuthentication,CustomAuthenticationForPublicUsersAndInvestigators
# Create your views here.
import datetime







class QueryListAPI(APIView):
    authentication_classes=(CustomAuthenticationForPublicUsersAndInvestigators,)
    permission_classes=(IsAuthenticated,)
    def get(self,request,format=None):
        obj=QueryModel.objects.all()
        serializer=QuerySerializer(obj,many=True)
        content={"flag":True,"serialized_data":serializer.data}
        return Response(content,status=status.HTTP_200_OK)



            
    def post(self,request,format=None):
        serializer=QuerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,"serialized_data":[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)  
        content={"flag":False,"serialized_data":[serializer.errors]}
        return Response(content,status=status.HTTP_200_OK)
 


class QueryDetailAPI(APIView):
    authentication_classes=(CustomTokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get_object(self,pk):
        try:
            return QueryModel.objects.get(pk=pk)
        except QueryModel.DoesNotExist:
            return False

    def get(self,request,pk,format=None):
        _obj=self.get_object(pk)
        if _obj==False:
            content={"flag":False,"serialized_data":[{"description":"IdDoesNotExists"}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        serializer=QuerySerializer(_obj)
        content={"flag":True,'serialized_data':[serializer.data]}
        print(serializer.data)
        return Response(content,status=status.HTTP_200_OK)
        
    def put(self,request,pk,format=None):
        _obj=self.get_object(pk)
        if _obj==False:
    
            content={"flag":False,"serialized_data":[{"description":"IdDoesNotExists"}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        serializer=QuerySerializer(_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def delete(self,request,pk,format=None):
        _obj=self.get_object(pk)
        _obj.delete()
        content={"flag":True}
        return Response(content,status=status.HTTP_200_OK)


