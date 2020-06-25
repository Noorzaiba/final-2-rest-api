from django.shortcuts import render
from rest_framework import serializers
from crime_reporting_scene_images_app.models import CrimeReportingSceneImages
from crime_reporting_app.models import CrimeReported
from crime_reporting_scene_images_app.serializers import CrimeReportingSceneImagesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from accounts.authentication import CustomTokenAuthentication
from images_app.views import DeleteImage
from accounts.authentication import CustomAuthentication,CustomTokenAuthentication,CustomAuthenticationForPublicUsersAndInvestigators
from public_users_app.permissions import CustomPermissionCheck




class CrimeReportingSceneImagesListAPI(APIView):
    authentication_classes=(CustomAuthenticationForPublicUsersAndInvestigators,)
    permission_classes=(IsAuthenticated,)
    def get(self,request,format=None):
        objs=CrimeReportingSceneImages.objects.all()
        serializer=CrimeReportingSceneImagesSerializer(objs,many=True)
        content={"flag":True,'serialized_data':serializer.data}
        return Response(content,status=status.HTTP_200_OK)
    

               
    def post(self,request,format=None):
        serializer=CrimeReportingSceneImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)
 

 

class CrimeReportingSceneImagesDetailAPI(APIView):
    authentication_classes=(CustomAuthenticationForPublicUsersAndInvestigators,)
    permission_classes=(IsAuthenticated,)
    
    def get_object(self,pk):
        try:
            return CrimeReportingSceneImages.objects.get(pk=pk)
        except CrimeReportingSceneImages.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        obj=self.get_object(pk)
        serializer=CrimeReportingSceneImagesSerializer(obj)
        content={"flag":True,'serialized_data':[serializer.data]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)


    def delete(self,request,pk,format=None):
        obj=self.get_object(pk)
        image_name=obj.image_name
        print("here is image name")
        print(image_name)
        obj.delete()
        d=DeleteImage()
        z=d.delete_image("crime_reporting_scene_pictures",image_name)
        print(z)
        content={"flag":True}
        print(content)
        return Response(content,status=status.HTTP_200_OK)







class CrimeReportingSceneImagesGetAllByCrimeidAPI(APIView):
    lookup_field='crime_id'
    authentication_classes=(CustomAuthenticationForPublicUsersAndInvestigators,)
    permission_classes=(IsAuthenticated,)
    def get_object(self,crime_id):
        try:
            obj=CrimeReportingSceneImages.objects.filter(crime_id=crime_id)
            return obj
        except CrimeReportingSceneImages.DoesNotExist:
            raise Http404
      
    def get(self, request,crime_id, format=None):
        obj = self.get_object(crime_id)
        serializer = CrimeReportingSceneImagesSerializer(obj,many=True)
        content={"flag":True,'serialized_data':serializer.data}
        return Response(content,status=status.HTTP_200_OK)
