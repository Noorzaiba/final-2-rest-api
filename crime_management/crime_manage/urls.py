
from django.urls import path,include
from crime_manage import views


urlpatterns = [
    path('investigator_list/', views.InvestigatorListAPI.as_view()),
    path('investigator_address_list/', views.InvestigatorAddressListAPI.as_view()),
    path('investigator_detail_api/<str:email>/', views.InvestigatorDetailAPI.as_view()),
    path('investigator_detail_by_pk_api/<int:pk>/', views.InvestigatorDetailByPkAPI.as_view()),
    path('investigator_address_detail_api/<int:resident_id>/', views.InvestigatorAddressDetailAPI.as_view()),
    path("index/<str:email_verification_token>/",views.emailVerification),
    path('investigator_administrative_list/', views.InvestigatorsAdministrativeDetailAPIList.as_view()),
    path('investigator_detail_admin_api/<int:pk>/', views.InvestigatorsAdministrativeDetailAPI.as_view()),
    path('investigator_detail_admin_get_api/<str:email>/', views.InvestigatorsAdministrativeDetailGETAPI.as_view()),


]

   

