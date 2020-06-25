
from django.urls import path,include
from password_reset import views


urlpatterns = [
   
    path("forgot_password/",views.PasswordResetAPI.as_view()),
    path("password_otp_verify/",views.PasswordOTPVerificationAPI.as_view()),
    path("password_update/",views.PasswordUpdateAPI.as_view()),
  

   
]
