from django.db import models
from crime_reporting_app.models import CrimeReported


class CrimeReportingSceneImages(models.Model):
    image_name=models.CharField(max_length=300)
    crime_id=models.ForeignKey(CrimeReported,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.image_name
