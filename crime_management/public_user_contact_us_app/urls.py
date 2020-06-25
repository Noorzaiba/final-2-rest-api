
from django.urls import path,include
from public_user_contact_us_app import views


urlpatterns = [
   
    path("qurey_list/",views.QueryListAPI.as_view()),
    path("query_detail_api/<int:pk>/",views.QueryDetailAPI.as_view()),
 

   
]
