from public_users_app.models import PublicUser
from rest_framework import authentication
from rest_framework import exceptions



class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self,request):
        username=request.META.get('HTTP_X_USERNAME')
        print(username)
        print("got printe in public user")
        if not username:
            raise exceptions.AuthenticationFailed("No such user")
        try:
            user=PublicUser.is_authenticated(username)
            print(user)
            
           
        except PublicUser.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")
        return (user,None)
        

