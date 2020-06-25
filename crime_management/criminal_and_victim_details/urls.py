
from django.urls import path
from criminal_and_victim_details import views


urlpatterns = [
    
    path('victim_list/', views.VictimListAPI.as_view()),
    path('victim_detail_api/<int:pk>/', views.VictimDetailAPI.as_view()),
    path('criminal_list/', views.CriminalListAPI.as_view()),
    path('criminal_detail_api/<int:pk>/', views.CriminalDetailAPI.as_view()),
    path('criminal_address_list/', views.CriminalAddressListAPI.as_view()),
    path('criminal_address_detail_api/<int:resident_id>/', views.CriminalAddressDetailAPI.as_view()),
    path('vicitm_address_list/', views.VictimAddressListAPI.as_view()),
    path('victim_address_detail_api/<int:resident_id>/', views.VictimAddressDetailAPI.as_view()),

   

   
   
]
