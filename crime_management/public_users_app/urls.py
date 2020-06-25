
from django.urls import path,include
from public_users_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('public_user_list_api/', views.PublicUserListAPI.as_view()),
    path('public_user_address_list_api/', views.PublicUserAddressListAPI.as_view()),
    path("index/<str:email_verification_token>/",views.emailVerification),
    path('public_user_detail_api/<str:email_id>/', views.PublicUserDetailAPI.as_view()),
    path('public_user_login_api/', views.PublicUserLoginAPI.as_view()),
    path('public_user_address_detail_api/<int:resident_id>/', views.PublicUserAddressDetailAPI.as_view()),
    path('image/', views.ImageAPI.as_view()),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)