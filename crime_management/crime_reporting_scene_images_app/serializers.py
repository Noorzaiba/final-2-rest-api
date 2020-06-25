from rest_framework import serializers
from crime_reporting_scene_images_app.models import CrimeReportingSceneImages
from crime_reporting_app.models import CrimeReported
from images_app.views import InsertImage


class CrimeReportingSceneImagesSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    crime_id=serializers.CharField(max_length=20)
    image_name=serializers.CharField(max_length=2000000000000)

    class Meta:
        model=CrimeReportingSceneImages
        fields=['id',"image_name",'crime_id']
       
    def create(self,validated_data):
        crime_id=validated_data["crime_id"]
        try:
            crime_obj=CrimeReported.objects.get(id=crime_id)
        except CrimeReported.DoesNotExist:
            dummy_obj=CrimeReportingSceneImages(image_name="Invalid_Crime_id")
            return dummy_obj    
        image_name_string=validated_data["image_name"]
        i=InsertImage()
        image_name_string=i.insert_image("crime_reporting_scene_pictures",image_name_string)
        obj=CrimeReportingSceneImages.objects.create(
                crime_id=crime_obj,
                image_name=image_name_string
               )
        return obj

       
