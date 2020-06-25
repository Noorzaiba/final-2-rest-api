from rest_framework import serializers
from cases_information.models import CrimeDetail,CrimeLocationDetail,CrimeLiveUpdation
from crime_manage.models import InvestigatorProfile
from django.shortcuts import get_object_or_404

class CrimeLocationDetailSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model=CrimeLocationDetail
        fields=['resident_id','id','location','city','state','zip_code','longitude','latitude']
       
        
   
    def create(self,validated_data):
        obj=CrimeLocationDetail.objects.create(location=validated_data['location'],resident_id=validated_data['resident_id'],city=validated_data['city'],state=validated_data['state'],zip_code=validated_data['zip_code'],latitude=validated_data['latitude'],longitude=validated_data['longitude'])
        return obj


    def update(self,instance,validated_data):
        instance.id=validated_data.get("id",instance.id)
        instance.resident_id=validated_data.get("resident_id",instance.resident_id)
        instance.location=validated_data.get("location",instance.location)
        instance.city=validated_data.get("city",instance.city)
        instance.state=validated_data.get("state",instance.state)
        instance.zip_code=validated_data.get("zip_code",instance.zip_code)
        instance.latitude=validated_data.get('latitude',instance.latitude)
        instance.longitude=validated_data.get('longitude',instance.longitude)
        instance.save()
        return instance
          


class CrimeDetailSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    investigator_id=serializers.EmailField(max_length=34)

    class Meta:
        model=CrimeDetail
        fields=('id','description','type_of_crime','doc','dou','date','time','status','investigator_id')
       


    def create(self,validated_data):
        email=validated_data["investigator_id"]
        try:
            investigator_obj=InvestigatorProfile.objects.get(email=email)
        except InvestigatorProfile.DoesNotExist:
            obj=CrimeDetail(description="Invalid Investigator id")
            return obj
        crime_obj=CrimeDetail.objects.create(investigator_id=investigator_obj,description=validated_data['description'],type_of_crime=validated_data['type_of_crime'],date=validated_data['date'],time=validated_data['time'],status=validated_data['status'])
        return crime_obj


    def update(self,instance,validated_data):
        email=validated_data["investigator_id"]
        try:
            investigator_obj=InvestigatorProfile.objects.get(email=email)
        except InvestigatorProfile.DoesNotExist:
            obj=CrimeDetail(description="Invalid Investigator id")
            return obj
    
        instance.id=validated_data.get('id',instance.id)
        instance.description=validated_data.get("description",instance.description)
        instance.date=validated_data.get("date",instance.date)
        instance.time=validated_data.get("time",instance.time)
        instance.status=validated_data.get("status",instance.status)
        instance.type_of_crime=validated_data.get("type_of_crime",instance.type_of_crime)
        instance.investigator_id=investigator_obj
        instance.save()
        return instance







class CrimeLiveUpdationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CrimeLiveUpdation
        fields=('id','crime_id','comments','doc',"dou")
