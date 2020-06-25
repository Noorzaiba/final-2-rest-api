from django.db import models
from cases_information.models import CrimeDetail


class CrimeSceneImages(models.Model):
    image_name=models.CharField(max_length=300)
    crime_id=models.ForeignKey(CrimeDetail,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.image_name
