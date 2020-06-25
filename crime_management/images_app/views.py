from django.shortcuts import render
from PIL import Image
from io import BytesIO
import base64
import os
from django.conf import settings
from django.utils.crypto import get_random_string
import datetime 
# Create your views here.

class InsertImage():
    def insert_image(self,location,image_string):
        print(location)
        image_data=image_string
        image_data_in_bytes=bytes(image_data,"utf-8")
        image_form=base64.decodestring(image_data_in_bytes)
        image=Image.open(BytesIO(image_form))
        now=str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        file_name=now+str(get_random_string(length=5,allowed_chars='123456789'))+".jpg"
        print(file_name)
        print(settings.MEDIA_ROOT)
        image.save(settings.MEDIA_ROOT+'/'+location+"/"+file_name)
        return file_name


class DeleteImage():

    def delete_image(self,location,image_name):
        print(location)
        print(image_name)
        try:
            path=settings.MEDIA_ROOT+'/'+location+"/"+image_name
            print("path :")
            print(path)
            m=os.remove(path)
            print(m)
            return True
        except Exception as e:
            print(e)
            print("No image was found")
            return False

        

