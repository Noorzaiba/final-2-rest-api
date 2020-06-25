from rest_framework import serializers
from crime_scene_images_app.models import CrimeSceneImages
from cases_information.models import CrimeDetail
from images_app.views import InsertImage


class CrimeSceneImagesSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    crime_id=serializers.CharField(max_length=20)
    image_name=serializers.CharField(max_length=2000000000000)

    class Meta:
        model=CrimeSceneImages
        fields=['id',"image_name",'crime_id']
       
    def create(self,validated_data):
        crime_id=validated_data["crime_id"]
        try:
            crime_obj=CrimeDetail.objects.get(id=crime_id)
        except CrimeDetail.DoesNotExist:
            dummy_obj=CrimeSceneImages(image_name="Invalid_Crime_id")
            return dummy_obj    
        image_name_string=validated_data["image_name"]
        i=InsertImage()
        image_name_string=i.insert_image("crime_scene_pictures",image_name_string)
        obj=CrimeSceneImages.objects.create(
                crime_id=crime_obj,
                image_name=image_name_string
               )
        return obj
        
       
