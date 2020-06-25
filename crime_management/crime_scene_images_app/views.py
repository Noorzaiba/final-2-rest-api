from django.shortcuts import render
from rest_framework import serializers
from crime_scene_images_app.models import CrimeSceneImages
from cases_information.models import CrimeDetail
from crime_scene_images_app.serializers import CrimeSceneImagesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from criminal_and_victim_details import models
from criminal_and_victim_details import serializers
from rest_framework.permissions import IsAuthenticated
from accounts.authentication import CustomTokenAuthentication
from images_app.views import DeleteImage




class CrimeSceneImagesListAPI(APIView):
    authentication_classes=(CustomTokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get(self,request,format=None):
        objs=CrimeSceneImages.objects.all()
        serializer=CrimeSceneImagesSerializer(objs,many=True)
        content={"flag":True,'serialized_data':serializer.data}
        return Response(content,status=status.HTTP_200_OK)
    

               
    def post(self,request,format=None):
        serializer=CrimeSceneImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)
 

 

class CrimeSceneImagesDetailAPI(APIView):
    authentication_classes=(CustomTokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get_object(self,pk):
        try:
            return CrimeSceneImages.objects.get(pk=pk)
        except CrimeSceneImages.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        obj=self.get_object(pk)
        serializer=CrimeSceneImagesSerializer(obj)
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
        z=d.delete_image("crime_scene_pictures",image_name)
        print(z)
        content={"flag":True}
        return Response(content,status=status.HTTP_200_OK)







class CrimeSceneImagesGetAllByCrimeidAPI(APIView):
    lookup_field='crime_id'
    def get_object(self,crime_id):
        try:
            obj=CrimeSceneImages.objects.filter(crime_id=crime_id)
            return obj
        except CrimeSceneImages.DoesNotExist:
            raise Http404
      
    def get(self, request,crime_id, format=None):
        obj = self.get_object(crime_id)
        serializer = CrimeSceneImagesSerializer(obj,many=True)
        content={"flag":True,'serialized_data':serializer.data}
        return Response(content,status=status.HTTP_200_OK)
