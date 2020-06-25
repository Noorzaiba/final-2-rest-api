from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from cases_information.serializers import CrimeDetailSerializer,CrimeLocationDetailSerializer,CrimeLiveUpdationSerializer
from cases_information.models import CrimeDetail,CrimeLocationDetail,CrimeLiveUpdation
from rest_framework import views
from django.http import Http404
from crime_scene_images_app.models import CrimeSceneImages
from accounts.authentication import CustomTokenAuthentication
from images_app.views import DeleteImage



class CrimeDetailListAPI(views.APIView):
    
    authentication_classes=(CustomTokenAuthentication,)
    def get(self,request,format=None):
        crime_objects=CrimeDetail.objects.all()
        serializer=CrimeDetailSerializer(crime_objects,many=True)
        content={"flag":True,'serialized_data_crime_register':serializer.data}
        return Response(content,status=status.HTTP_200_OK)


               
    def post(self,request,format=None):
        serializer=CrimeDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data_crime_register':[serializer.data]}
            return Response(content,status=status.HTTP_200_OK)
        print(serializer.errors)
        content={"flag":False,'serialized_data_crime_register':[serializer.errors]}
        return Response(content,status=status.HTTP_200_OK)
 

 



class CrimeLocationAddressListAPI(views.APIView):
    authentication_classes=(CustomTokenAuthentication,)
    def get(self,request,format=None):
        address=CrimeLocationDetail.objects.all()
        serializer=CrimeLocationDetailSerializer(address,many=True)
        content={"flag":True,"serialized_data":serializer.data}
        return Response(content,status=status.HTTP_200_OK)



            
    def post(self,request,format=None):
        serializer=CrimeLocationDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,"serialized_data":[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)  
        content={"flag":False,"serialized_data":[serializer.errors]}
        return Response(content,status=status.HTTP_200_OK)
 






class CrimeLocationAddressDetailAPI(views.APIView):
    lookup_field='resident_id'
    authentication_classes=(CustomTokenAuthentication,)
    def get_object(self,resident_id):
        try:
            return CrimeLocationDetail.objects.get(resident_id=resident_id)
        except CrimeLocationDetail.DoesNotExist:
            return False

    def get(self,request,resident_id,format=None):
        inv_address_obj=self.get_object(resident_id)
        if inv_address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        print("sentered")
        serializer=CrimeLocationDetailSerializer(inv_address_obj)
        content={"flag":True,"serialized_data":[serializer.data]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def put(self,request,resident_id,format=None):
        inv_address_obj=self.get_object(resident_id)
        if inv_address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        serializer=CrimeLocationDetailSerializer(inv_address_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def delete(self,request,resident_id,format=None):
        inv_address_obj=self.get_object(resident_id)
        if inv_address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            print("im getting deleted1")
            return Response(content,status=status.HTTP_200_OK)
        inv_address_obj.delete()
        content={"flag":True}
        return Response(content,status=status.HTTP_200_OK)




class CrimeDetailAPI(views.APIView):
    authentication_classes=(CustomTokenAuthentication,)
    def get_object(self,pk):
        try:
            return CrimeDetail.objects.get(pk=pk)
        except CrimeDetail.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        crime_obj=self.get_object(pk)
        serializer=CrimeDetailSerializer(crime_obj)
        content={"flag":True,'serialized_data_crime_register':[serializer.data]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        crime_obj=self.get_object(pk)
        serializer=CrimeDetailSerializer(crime_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data_crime_register':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data_crime_register':[serializer.data]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def delete(self,request,pk,format=None):
        crime_obj=self.get_object(pk)
        try:
            obj_list=CrimeSceneImages.objects.filter(crime_id=crime_obj)
            delete_images(obj_list)
            print("im getting deleted1")
            crime_obj.delete()
            content={"flag":True}
            return Response(content,status=status.HTTP_200_OK)
        except CrimeSceneImages.DoesNotExist:
            crime_obj.delete()
            content={"flag":True}
            return Response(content,status=status.HTTP_200_OK)
        

def delete_images(obj_list):
    d=DeleteImage()
    for i in obj_list:
        d.delete_image("crime_scene_pictures",i.image_name)
       
  


class CrimeLiveUpdationListAPI(views.APIView):
    authentication_classes=(CustomTokenAuthentication,)
    def get(self, request, format=None):
        crime_list = CrimeLiveUpdation.objects.all()
        serializer = CrimeLiveUpdationSerializer( crime_list, many=True)
        content={"flag":True,'serialized_data':serializer.data}
        return Response(content,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CrimeLiveUpdationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        return Response(content, status=status.HTTP_200_OK)


class  CrimeLiveUpdationDetailAPI(views.APIView):
    authentication_classes=(CustomTokenAuthentication,)
    def get_object(self, pk):
        try:
            return CrimeLiveUpdation.objects.get(pk=pk)
        except CrimeLiveUpdation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        crime_list = self.get_object(pk)
        serializer = CrimeLiveUpdationSerializer(crime_list)
        content={"flag":True,'serialized_data':[serializer.data]}
        return Response(content,status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        crime_list = self.get_object(pk)
        serializer =CrimeLiveUpdationSerializer(crime_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        return Response(content, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    




