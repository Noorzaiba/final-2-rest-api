
from django.urls import path,include
from crime_reporting_app import views

urlpatterns = [
    path("crime_reported_address_list/",views.CrimeReportedAddressListAPI.as_view()), 
    path("crime_reported_list/",views.CrimeReportedListAPI.as_view()),  
    path("crime_reported_detail/<int:pk>/",views.CrimeReportedDetailAPI.as_view()),
    path("crime_reported_user_detail/<str:email_id>/",views.CrimeReportedDetailUserRetrieveAPI.as_view()),
    path("crime_reported_address_detail/<int:resident_id>/",views.CrimeReportedAddressDetailAPI.as_view()),
    path("crime_reported_final_submit/",views.CrimeReportedFinalSubmitAPI.as_view()),
    path("crime_reported_unsubmit/<str:email_id>/",views.CrimeReportedUnSubmitAPI.as_view()),
   
   

]