from crime_manage.models import InvestigatorProfile
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from public_users_app.models import PublicUser


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self,request):
        username=request.META.get('HTTP_X_USERNAME')
        incoming_token=request.META.get("HTTP_AUTHORIZATION")
        print(incoming_token)
        print(username)
        print("got printed in Custom Authentication")
        if not username:
            return None
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
        print(incoming_token)
        print("got printed in Custom Token Authentication")
        
        try:
            user=InvestigatorProfile.objects.get(email=username)
            print(user)
        except InvestigatorProfile.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")
        token,created=Token.objects.get_or_create(user=user)
        print(token.key==incoming_token)
        if token.key!=incoming_token:
            raise exceptions.AuthenticationFailed("No such user")
        return(user,None)



class CustomAuthenticationForPublicUsersAndInvestigators(authentication.BaseAuthentication):
    def authenticate(self,request):
        username=request.META.get('HTTP_X_USERNAME')
        print(username)
        print("got printed in both")
        if not username:
            return None
        try:
            invest_obj=InvestigatorProfile.objects.get(email=username)
        except InvestigatorProfile.DoesNotExist:
            print("no invest")
            try:
                public_obj=PublicUser.objects.get(email_id=username)
            except PublicUser.DoesNotExist:
                print("no public user")
                raise exceptions.AuthenticationFailed("No such user")
            return(public_obj,None)
            raise exceptions.AuthenticationFailed("No such user")
        return (invest_obj,None)

  
        
       
            




        
