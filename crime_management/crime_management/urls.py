"""crime_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('crime_manage/',include('crime_manage.urls')),
    path('cases_info/',include('cases_information.urls')),
    path('password_reset/',include('password_reset.urls')),
    path('password_reset_for_public_users/',include('password_reset_for_public_users.urls')),
    path("accounts/",include("accounts.urls")),
    path("criminal_victim_details/",include("criminal_and_victim_details.urls")),
    path("public_users_api/",include("public_users_app.urls")),
    path("crime_reporting/",include("crime_reporting_app.urls")),
    path("public_user_contact_us/",include("public_user_contact_us_app.urls")),
    path("investigator_contact_us/",include("investigator_contact_us_app.urls")),
    path("crime_scene_pictures/",include("crime_scene_images_app.urls")),
    path("crime_reporting_scene_pictures/",include("crime_reporting_scene_images_app.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()


