from rest_framework import serializers
from crime_reporting_app.models import CrimeReported,CrimeReportedLocation
from public_users_app.models import PublicUser
 



class CrimeReportedLocationSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    
    class Meta:
        model=CrimeReportedLocation
        fields=['resident_id','id','location','city','state','zip_code','latitude','longitude']

    def create(self,validated_data):
        crime_address_obj=CrimeReportedLocation.objects.create(location=validated_data['location'],resident_id=validated_data['resident_id'],city=validated_data['city'],state=validated_data['state'],zip_code=validated_data['zip_code'],latitude=validated_data['latitude'],longitude=validated_data['longitude'])
        return crime_address_obj



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
  




class CrimeReportedSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=CrimeReported
        fields=('id','description','type_of_crime','doc','dou','date','time','status','user',"final_submit")
    id=serializers.IntegerField(required=False)
    user=serializers.CharField(max_length=50)
   

    def create(self,validated_data):
        email=validated_data['user']
        print(email)
        print(validated_data["final_submit"])
        try:
           obj=PublicUser.objects.get(email_id=email)
        except PublicUser.DoesNotExist:
            obj=CrimeReported(description="userDoesExists@gmail.com")
            print(obj)
            return obj
        crime_obj=CrimeReported.objects.create(final_submit=validated_data["final_submit"],description=validated_data['description'],type_of_crime=validated_data['type_of_crime'],date=validated_data['date'],time=validated_data['time'],status="Crime Reported",user=obj)
        return crime_obj


   

       


    def update(self,instance,validated_data):
        email=validated_data["user"]
        try:
            obj=PublicUser.objects.get(email_id=email)
        except PublicUser.DoesNotExist:
            obj=CrimeReported(description="userDoesExists@gmail.com")
            return obj
        instance.id=validated_data.get('id',instance.id)
        instance.description=validated_data.get("description",instance.description)
        instance.date=validated_data.get("date",instance.date)
        instance.time=validated_data.get("time",instance.time)
        instance.status=validated_data.get("status",instance.status)
        instance.type_of_crime=validated_data.get("type_of_crime",instance.type_of_crime)
        instance.user=obj
        instance.save()
        return instance




class CrimeReportingFinalSubmitSerializer(serializers.Serializer):
    final_submit=serializers.BooleanField()
    id=serializers.IntegerField()
    
    def create(self,validated_data):
        try:
           print(validated_data["id"]);
           print(validated_data["final_submit"]);
           obj=CrimeReported.objects.get(id=validated_data["id"])
           obj.final_submit=validated_data["final_submit"]
           obj.save()
           return obj
        except CrimeReported.DoesNotExist:
            obj=CrimeReported(description="invalid_id")
            print(obj)
            return obj


        
