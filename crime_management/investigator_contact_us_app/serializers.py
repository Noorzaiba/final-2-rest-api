
from rest_framework import serializers
from investigator_contact_us_app import models
from crime_manage.models import InvestigatorProfile

class QuerySerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    email=serializers.CharField(max_length=1000)
  
    class Meta:
        model=models.QueryModel
        fields=['id','description',"status",'email','doc','dou']
        

    def create(self,validated_data):
        email=validated_data['email']
        try:
            _obj=InvestigatorProfile.objects.get(email=email)
        except InvestigatorProfile.DoesNotExist:
            dummy_obj=models.QueryModel(description="Invalid Email Id")
            return dummy_obj
        query_obj=models.QueryModel.objects.create(
        description=validated_data['description'],
        status=validated_data["status"],
        email=_obj)
        return query_obj


    def update(self,instance,validated_data):
        email=validated_data['email']
        try:
            _obj=InvestigatorProfile.objects.get(email=email)
        except InvestigatorProfile.DoesNotExist:
            dummy_obj=models.QueryModel(description="Invalid Email Id")
            return dummy_obj
        print("im here")
        instance.id=validated_data.get("id",instance.id)
        instance.description=validated_data.get("description",instance.description)
        instance.status=validated_data.get("status",instance.status)
        instance.email=_obj
        instance.doc=validated_data.get("doc",instance.doc)
        instance.dou=validated_data.get("dou",instance.dou)
        instance.save()
        return instance
                   
    