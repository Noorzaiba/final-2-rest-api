from crime_manage.models import InvestigatorProfile
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self,request):
        username=request.META.get('HTTP_X_USERNAME')
        print(username)
        print("got printed in investigator1")
        if not username:
            raise exceptions.AuthenticationFailed("No such user")
        try:
            user=InvestigatorProfile.objects.get(email=username)
            print(user)
        except InvestigatorProfile.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")
        return (user,None)
        


class CustomTokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self,request):
        incoming_token=request.META.get("HTTP_AUTHORIZATION")
        username=request.META.get('HTTP_X_USERNAME')
        print(username)
        print("got printed in investigator2")
        user=InvestigatorProfile.objects.get(email=username)
        token,created=Token.objects.get_or_create(user=user)
        print(token.key==incoming_token)
        if token.key!=incoming_token:
            raise exceptions.AuthenticationFailed("No such user")
        return(user,None)

