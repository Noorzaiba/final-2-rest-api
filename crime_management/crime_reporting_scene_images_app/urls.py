from django.urls import path,include
from crime_reporting_scene_images_app import views


urlpatterns = [
    path('crime_reporting_scene_images_list/', views.CrimeReportingSceneImagesListAPI.as_view()),
    path('crime_reporting_scene_images_detail/<int:pk>/', views.CrimeReportingSceneImagesDetailAPI.as_view()),
    path('crime_reporting_scene_images/<int:crime_id>/', views.CrimeReportingSceneImagesGetAllByCrimeidAPI.as_view()),
 

]

   