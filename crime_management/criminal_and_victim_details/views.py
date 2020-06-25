from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from criminal_and_victim_details import models
from criminal_and_victim_details import serializers
from rest_framework.permissions import IsAuthenticated
from images_app.views import DeleteImage


from accounts.authentication import CustomTokenAuthentication
# Create your views here.


class VictimListAPI(APIView):
    authentication_classes=(CustomTokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get(self,request,format=None):
        victims=models.VictimDetail.objects.all()
        serializer=serializers.VictimDetailSerializer(victims,many=True)
        content={"flag":True,'serialized_data':serializer.data}
        print(content)
        return Response(content,status=status.HTTP_200_OK)
    

               
    def post(self,request,format=None):
        serializer=serializers.VictimDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)
 

 


class VictimDetailAPI(APIView):
    authentication_classes=(CustomTokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get_object(self,pk):
        try:
            return models.VictimDetail.objects.get(pk=pk)
        except models.VictimDetail.DoesNotExist:
            raise Http404


    def get(self,request,pk,format=None):
        victim_obj=self.get_object(pk)
        serializer=serializers.VictimDetailSerializer(victim_obj)
        content={"flag":True,'serialized_data':[serializer.data]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        victim_obj=self.get_object(pk)
        serializer=serializers.VictimDetailSerializer(victim_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)
    def delete(self,request,pk,format=None):
        victim_obj=self.get_object(pk)
        image_name=victim_obj.profile_image
        try:
            #if victim record has been transferred to criminal record
            models.CriminalDetail.objects.get(profile_image=image_name)
            print("no deleting of image")
            victim_obj.delete()
            content={"flag":True}
            return Response(content,status=status.HTTP_200_OK)
        except models.CriminalDetail.DoesNotExist:
            print("here is image name")
            print(image_name)
            d=DeleteImage()
            z=d.delete_image("victim_criminal_profile_pictures",image_name)
            print(z)
            print(" deleting of image")
            victim_obj.delete()
            content={"flag":True}
            return Response(content,status=status.HTTP_200_OK)

     




class CriminalListAPI(APIView):
    authentication_classes=(CustomTokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get(self,request,format=None):
        criminals=models.CriminalDetail.objects.all()
        serializer=serializers.CriminalDetailSerializer(criminals,many=True)
        content={"flag":True,'serialized_data':serializer.data}
        return Response(content,status=status.HTTP_200_OK)
    

               
    def post(self,request,format=None):
        serializer=serializers.CriminalDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)
 

 


class CriminalDetailAPI(APIView):
    authentication_classes=(CustomTokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get_object(self,pk):
        try:
            return models.CriminalDetail.objects.get(pk=pk)
        except models.CriminalDetail.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        criminal_obj=self.get_object(pk)
        serializer=serializers.CriminalDetailSerializer(criminal_obj)
        content={"flag":True,'serialized_data':[serializer.data]}
        print(serializer.data)
        return Response(content,status=status.HTTP_200_OK)
        
    def put(self,request,pk,format=None):
        criminal_obj=self.get_object(pk)
        serializer=serializers.CriminalDetailSerializer(criminal_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def delete(self,request,pk,format=None):
        criminal_obj=self.get_object(pk)
        image_name=criminal_obj.profile_image
        try:
            #if criminal record has been transferred to victim record
            models.VictimDetail.objects.get(profile_image=image_name)
            print("no deleting of image")
            criminal_obj.delete()
            content={"flag":True}
            return Response(content,status=status.HTTP_200_OK)
        except models.VictimDetail.DoesNotExist:
            print("here is image name")
            print(image_name)
            d=DeleteImage()
            z=d.delete_image("victim_criminal_profile_pictures",image_name)
            print(z)
            print(" deleting of image")
            criminal_obj.delete()
            content={"flag":True}
            return Response(content,status=status.HTTP_200_OK)

            
        
        





class VictimAddressListAPI(APIView):
    authentication_classes=(CustomTokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get(self,request,format=None):
        address=models.VictimDetailAddress.objects.all()
        serializer=serializers.VictimDetailAddressSerializer(address,many=True)
        content={"flag":True,"serialized_data":serializer.data}
        return Response(content,status=status.HTTP_200_OK)



            
    def post(self,request,format=None):
        serializer=serializers.VictimDetailAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,"serialized_data":[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)  
        content={"flag":False,"serialized_data":[serializer.errors]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)
 



class CriminalAddressListAPI(APIView):
    authentication_classes=(CustomTokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get(self,request,format=None):
        address=models.CriminalDetailAddress.objects.all()
        serializer=serializers.CriminalDetailAddressSerializer(address,many=True)
        content={"flag":True,"serialized_data":serializer.data}
        print(content)
        return Response(content,status=status.HTTP_200_OK)



            
    def post(self,request,format=None):
        serializer=serializers.CriminalDetailAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,"serialized_data":[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)  
        content={"flag":False,"serialized_data":[serializer.errors]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)
 






class VictimAddressDetailAPI(APIView):
    lookup_field='resident_id'
    authentication_classes=(CustomTokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get_object(self,resident_id):
        try:
            return models.VictimDetailAddress.objects.get(resident_id=resident_id)
        except models.VictimDetailAddress.DoesNotExist:
            return False

    def get(self,request,resident_id,format=None):
        address_obj=self.get_object(resident_id)
        if address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        print("sentered")
        serializer=serializers.VictimDetailAddressSerializer(address_obj)
        content={"flag":True,"serialized_data":[serializer.data]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def put(self,request,resident_id,format=None):
        address_obj=self.get_object(resident_id)
        if address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        serializer=serializers.VictimDetailAddressSerializer(address_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def delete(self,request,resident_id,format=None):
        address_obj=self.get_object(resident_id)
        if address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        address_obj.delete()
        content={"flag":True,}
        return Response(content,status=status.HTTP_200_OK)




class CriminalAddressDetailAPI(APIView):
    lookup_field='resident_id'
    authentication_classes=(CustomTokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get_object(self,resident_id):
        try:
            return models.CriminalDetailAddress.objects.get(resident_id=resident_id)
        except models.CriminalDetailAddress.DoesNotExist:
            return False

    def get(self,request,resident_id,format=None):
        address_obj=self.get_object(resident_id)
        if address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        print("sentered")
        serializer=serializers.CriminalDetailAddressSerializer(address_obj)
        content={"flag":True,"serialized_data":[serializer.data]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def put(self,request,resident_id,format=None):
        address_obj=self.get_object(resident_id)
        if address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        serializer=serializers.CriminalDetailAddressSerializer(address_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def delete(self,request,resident_id,format=None):
        address_obj=self.get_object(resident_id)
        if address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        address_obj.delete()
        content={"flag":True,}
        return Response(content,status=status.HTTP_200_OK)


