from django.urls import path,include
from crime_scene_images_app import views


urlpatterns = [
    path('crime_scene_images_list/', views.CrimeSceneImagesListAPI.as_view()),
    path('crime_scene_images_detail/<int:pk>/', views.CrimeSceneImagesDetailAPI.as_view()),
    path('crime_scene_images/<int:crime_id>/', views.CrimeSceneImagesGetAllByCrimeidAPI.as_view()),
 

]

   