from django.shortcuts import render
from crime_reporting_app.models import CrimeReported,CrimeReportedLocation
from public_users_app.models import PublicUser
from crime_reporting_app.serializers import CrimeReportedSerializer,CrimeReportedLocationSerializer,CrimeReportingFinalSubmitSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from accounts.authentication import CustomAuthentication,CustomTokenAuthentication,CustomAuthenticationForPublicUsersAndInvestigators
from public_users_app.permissions import CustomPermissionCheck






class CrimeReportedListAPI(views.APIView):
    authentication_classes=(CustomAuthenticationForPublicUsersAndInvestigators,)
    permission_classes=(IsAuthenticated,)
    def get(self,request,format=None):
        crime_objects=CrimeReported.objects.all()
        serializer=CrimeReportedSerializer(crime_objects,many=True)
        content={"flag":True,'serialized_data_crime_reported':serializer.data}
        print(content)
        return Response(content,status=status.HTTP_200_OK)


               
    def post(self,request,format=None):
        serializer=CrimeReportedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data_crime_reported':[serializer.data]}
            return Response(serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        content={"flag":False,'serialized_data_crime_reported':[serializer.errors]}
        return Response(serializer.data,status=status.HTTP_200_OK)




class CrimeReportedAddressListAPI(views.APIView):
    authentication_classes=(CustomAuthenticationForPublicUsersAndInvestigators,)
    permission_classes=(IsAuthenticated,)
    def get(self,request,format=None):
        crime_address_objects=CrimeReportedLocation.objects.all()
        serializer=CrimeReportedLocationSerializer(crime_address_objects,many=True)
        content={"flag":True,'serialized_data_crime_reported':serializer.data}
        return Response(serializer.data,status=status.HTTP_200_OK)


               
    def post(self,request,format=None):
        serializer=CrimeReportedLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data_crime_reported':[serializer.data]}
            return Response(serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        content={"flag":False,'serialized_data_crime_reported':[serializer.errors]}
        return Response(serializer.data,status=status.HTTP_200_OK)





class CrimeReportedDetailAPI(views.APIView):
    authentication_classes=(CustomAuthenticationForPublicUsersAndInvestigators,)
    permission_classes=(IsAuthenticated,)
    def get_object(self,pk):
        try:
            return CrimeReported.objects.get(pk=pk)
        except CrimeReported.DoesNotExist:
            raise Http404
       
    def get(self,request,pk,format=None):
        crime_obj=self.get_object(pk)
        serializer=CrimeReportedSerializer(crime_obj)
        content={"flag":True,'serialized_data_crime_reported':[serializer.data]}
        print(content)
        print("*******************")
        return Response(content,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        crime_obj=self.get_object(pk)
        serializer=CrimeReportedSerializer(crime_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data_crime_reported':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        content={"flag":False,'serialized_data_crime_reported':[serializer.data]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def delete(self,request,pk,format=None):
        crime_obj=self.get_object(pk)
        crime_obj.delete()
        content={"flag":True}
        return Response(content,status=status.HTTP_200_OK)



 
 


class CrimeReportedDetailUserRetrieveAPI(views.APIView):
    look_up="email_id"
    authentication_classes=(CustomAuthenticationForPublicUsersAndInvestigators,)
    permission_classes=(IsAuthenticated,)
    def get_object(self,email_id):
        try:
            user=PublicUser.objects.get(email_id=email_id)
            return CrimeReported.objects.filter(user=user,final_submit=True)
        except CrimeReported.DoesNotExist:
            return False
        except PublicUser.DoesNotExist:
            return False
       
    def get(self,request,email_id,format=None):
        crime_obj=self.get_object(email_id)
        if crime_obj==False:
            content={"flag":False,'serialized_data_crime_reported':False}
            return Response(content,status=status.HTTP_200_OK)
        else:
            serializer=CrimeReportedSerializer(crime_obj,many=True)
            content={"flag":True,'serialized_data_crime_reported':serializer.data}
            return Response(content,status=status.HTTP_200_OK)

        


class CrimeReportedAddressDetailAPI(views.APIView):
    lookup_field='resident_id'
    authentication_classes=(CustomAuthenticationForPublicUsersAndInvestigators,)
    permission_classes=(IsAuthenticated,)
    def get_object(self,resident_id):
        try:
            return CrimeReportedLocation.objects.get(resident_id=resident_id)
        except CrimeReportedLocation.DoesNotExist:
            return False

    def get(self,request,resident_id,format=None):
        address_obj=self.get_object(resident_id)
        if  address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        print("sentered")
        serializer=CrimeReportedLocationSerializer(address_obj)
        content={"flag":True,"serialized_data":[serializer.data]}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

    def put(self,request,resident_id,format=None):
        address_obj=self.get_object(resident_id)
        if  address_obj==False:
            content={"flag":False,"serialized_data":[{"location":"AddressDoesNotExists","resident_id":resident_id}]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        serializer=CrimeReportedLocationSerializer(address_obj,data=request.data)
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
        address_obj.delete()
        content={"flag":True,}
        return Response(content,status=status.HTTP_200_OK)



class CrimeReportedFinalSubmitAPI(views.APIView):
   

               
    def post(self,request,format=None):
        serializer=CrimeReportingFinalSubmitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={"flag":True,'serialized_data_crime_reported':[serializer.data]}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        print(serializer.errors)
        content={"flag":False,'serialized_data_crime_reported':[serializer.errors]}
        return Response(content,status=status.HTTP_200_OK)




class CrimeReportedUnSubmitAPI(views.APIView):
    look_up="email_id"
    #authentication_classes=(CustomAuthenticationForPublicUsersAndInvestigators,)
    #permission_classes=(IsAuthenticated,)
    def get_object(self,email_id):
        try:
            user=PublicUser.objects.get(email_id=email_id)          
            obj_list=CrimeReported.objects.filter(user=user,final_submit=False)
            return obj_list
        except CrimeReported.DoesNotExist:
            raise Http404
        except PublicUser.DoesNotExist:
            raise Http404e
       
    def get(self,request,email_id,format=None):
        crime_obj=self.get_object(email_id)
        if crime_obj==False:
            content={"flag":False,'serialized_data_crime_reported':False}
            print(content)
            return Response(content,status=status.HTTP_200_OK)
        else:
            serializer=CrimeReportedSerializer(crime_obj,many=True)
            content={"flag":True,'serialized_data_crime_reported':serializer.data}
            print(content)
            return Response(content,status=status.HTTP_200_OK)

        
       