from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from crime_manage.serializers import InvestigatorAddressSerializer,InvestigatorDetailSerializer,InvestigatorsAdministrativeDetailSerializer
from rest_framework.settings import api_settings
from crime_manage.models import InvestigatorProfile,InvestigatorAddress,InvestigatorsAdministrativeDetail
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from accounts.authentication import CustomAuthentication,CustomTokenAuthentication
from django.http import Http404
from images_app.views import DeleteImage




def emailVerification(request,email_verification_token):
    print(email_verification_token+ "in index")
    if email_verification_token:
        obj=get_object_or_404(InvestigatorProfile,email_verification_token=email_verification_token)
        print(obj.status)
        obj.status=True
        obj.email_verification_token="null"
        obj.save()
        print(obj.status)
        return render(request,"crime_manage/index.html",{"email_verification_token":email_verification_token,"success":'Email successfully verified'})
    return render(request,"crime_manage/index.html",{"email_verification_token":email_verification_token,"success":"Unsucess at Email verification plz register agian"})


class InvestigatorListAPI(APIView):
    
    def get(self,request,format=None):
        investigators=InvestigatorProfile.objects.all()
        serializer=InvestigatorDetailSerializer(investigators,many=True)
        content={"flag":True,"serialized_investigator_register_data":serializer.data}
        return Response(content,status=status.HTTP_200_OK)
 
            
    def post(self,request,format=None):
        serializer=InvestigatorDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,"serialized_investigator_register_data":[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        errors_in_process=serializer.errors['email']
        print(errors_in_process)
        s=errors_in_process[0]
        print(s)
        content={"flag":False,"serialized_investigator_register_data":[{'email':s}]}
        print(serializer.errors)
        return Response(content,status=status.HTTP_200_OK)
 
    
 


class InvestigatorAddressListAPI(APIView):
    def get(self,request,format=None):
        investigator_address=InvestigatorAddress.objects.all()
        serializer=InvestigatorAddressSerializer(investigator_address,many=True)
        content={"flag":True,"serialized_data":serializer.data}
        return Response(content,status=status.HTTP_200_OK)



            
    def post(self,request,format=None):
        serializer=InvestigatorAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,"serialized_data":[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)  
        content={"flag":False,"serialized_data":[serializer.errors]}
        return Response(content,status=status.HTTP_200_OK)
 



class InvestigatorDetailByPkAPI(APIView):
   
    authentication_classes=(CustomTokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get_object(self,pk):
        try:
            print("here")
            return InvestigatorProfile.objects.get(pk=pk)
        except InvestigatorProfile.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        investigator_obj=self.get_object(pk)
        print("sentered")
        serializer=InvestigatorDetailSerializer(investigator_obj)
        print("here1")
        content={"flag":True,"serialized_investigator_register_data":[serializer.data]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        investigator_obj=self.get_object(pk)
        print(request.META.get("HTTP_AUTHORIZATION"))
        serializer=InvestigatorDetailSerializer(investigator_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_investigator_register_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        errors_in_process=serializer.errors['email']
        print(errors_in_process)
        s=errors_in_process[0]
        print(s)
        content={"flag":False,"serialized_investigator_register_data":[{'email':s}]}
        return Response(content,status=status.HTTP_200_OK)
      

    def delete(self,request,pk,format=None):
        investigator_obj=self.get_object(pk)
        image_name=investigator_obj.profile_image
        investigator_obj.delete()
        print("here is image name")
        print(image_name)
        d=DeleteImage()
        z=d.delete_image("investigator_profile_pictures",image_name)
        print(z)
        content={"flag":True}
        return Response(content,status=status.HTTP_200_OK)






class InvestigatorDetailAPI(APIView): 
    lookup_field='email'
    authentication_classes=(CustomTokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get_object(self,email):
        try:
            print("here")
            return InvestigatorProfile.objects.get(email=email)
        except InvestigatorProfile.DoesNotExist:
            raise Http404

    def get(self,request,email,format=None):
        investigator_obj=self.get_object(email)
        print("sentered")
        serializer=InvestigatorDetailSerializer(investigator_obj)
        print("here1")
        content={"flag":True,"serialized_investigator_register_data":[serializer.data]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def put(self,request,email,format=None):
        investigator_obj=self.get_object(email)
        print(request.META.get("HTTP_AUTHORIZATION"))
        serializer=InvestigatorDetailSerializer(investigator_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_investigator_register_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        errors_in_process=serializer.errors['email']
        print(errors_in_process)
        s=errors_in_process[0]
        print(s)
        content={"flag":False,"serialized_investigator_register_data":[{'email':s}]}
        return Response(content,status=status.HTTP_200_OK)
      

    def delete(self,request,email,format=None):
        investigator_obj=self.get_object(email)
        image_name=investigator_obj.profile_image
        investigator_obj.delete()
        print("here is image name")
        print(image_name)
        d=DeleteImage()
        z=d.delete_image("investigator_profile_pictures",image_name)
        print(z)
        content={"flag":True}
        return Response(content,status=status.HTTP_200_OK)





  




class InvestigatorAddressDetailAPI(APIView):
    lookup_field='resident_id'
    authentication_classes=(CustomAuthentication,CustomTokenAuthentication)
    permission_classes=(IsAuthenticated,)
    def get_object(self,resident_id):
        try:
            return InvestigatorAddress.objects.get(resident_id=resident_id)
        except InvestigatorAddress.DoesNotExist:
            return False

    def get(self,request,resident_id,format=None):
        inv_address_obj=self.get_object(resident_id)
        if inv_address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        print("sentered")
        serializer=InvestigatorAddressSerializer(inv_address_obj)
        content={"flag":True,"serialized_data":[serializer.data]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def put(self,request,resident_id,format=None):
        inv_address_obj=self.get_object(resident_id)
        if inv_address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        serializer=InvestigatorAddressSerializer(inv_address_obj,data=request.data)
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
            return Response(content,status=status.HTTP_200_OK)
        inv_address_obj.delete()
        content={"flag":True,}
        return Response(content,status=status.HTTP_200_OK)






class InvestigatorsAdministrativeDetailAPIList(APIView):
   
    def get(self, request, format=None):
        lists = InvestigatorsAdministrativeDetail.objects.all()
        serializer=InvestigatorsAdministrativeDetailSerializer(lists, many=True)
        content={"flag":True,'serialized_data':serializer.data}
        return Response(content,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        print("hello")
        serializer = InvestigatorsAdministrativeDetailSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        print(content)
        return Response(content, status=status.HTTP_200_OK)

    
 

class InvestigatorsAdministrativeDetailAPI(APIView):
  
    def get_object(self, pk):
        try:
            return InvestigatorsAdministrativeDetail.objects.get(pk=pk)
        except InvestigatorsAdministrativeDetail.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = InvestigatorsAdministrativeDetailSerializer(obj)
        content={"flag":True,'serialized_data':[serializer.data]}
        return Response(content,status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer =InvestigatorsAdministrativeDetailSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data':[serializer.errors]}
        print(content)
        return Response(content, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_200_OK)

    




class InvestigatorsAdministrativeDetailGETAPI(APIView):
    lookup_field='email'
    def get_object(self,email):
        try:
            invst_obj=InvestigatorProfile.objects.get(email=email)
            return InvestigatorsAdministrativeDetail.objects.get(email=invst_obj)
        except InvestigatorsAdministrativeDetail.DoesNotExist:
            raise Http404
        except InvestigatorProfile.DoesNotExist:
            raise Http404

    def get(self, request,email, format=None):
        obj = self.get_object(email)
        serializer = InvestigatorsAdministrativeDetailSerializer(obj)
        content={"flag":True,'serialized_data':[serializer.data]}
        return Response(content,status=status.HTTP_200_OK)
