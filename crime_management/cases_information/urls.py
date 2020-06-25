
from django.urls import path,include
from cases_information import views

urlpatterns = [
    path("crime_list/",views.CrimeDetailListAPI.as_view()),  
    path('crime_detail_api/<int:pk>/', views.CrimeDetailAPI.as_view()), 
    path("crime_update_live/",views.CrimeLiveUpdationListAPI.as_view()),  
    path('crime_update_live_detail/<int:pk>/', views.CrimeLiveUpdationDetailAPI.as_view()),
    path('crime_location_address_list/', views.CrimeLocationAddressListAPI.as_view()),
    path('crime_location_address_detail_api/<int:resident_id>/', views.CrimeLocationAddressDetailAPI.as_view()),
    
]
