from rest_framework import permissions
from public_users_app.models import PublicUser


class CustomPermissionCheck(permissions.BasePermission):

    def has_permission(self,request,view):
        email=request.META.get('HTTP_X_USERNAME')
        print(email)
        print("in public user")
        valid=PublicUser.objects.filter(email_id=email).exists()
        return  valid
