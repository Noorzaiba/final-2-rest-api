from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings

class SendMailClass():
    def generate_random_string(self):
        unique_id=get_random_string(length=7)
        print("token: "+unique_id)
        return unique_id

    def generate_random_number(self):
        unique_id=get_random_string(length=7,allowed_chars='123456789')
        print("otp"+str(unique_id))
        return unique_id



    def send_email_for_verification(self,send_email_to, email_verification_token):
        print(" in send email"+email_verification_token)
        print("send to email"+send_email_to)
        from_email=settings.EMAIL_HOST_USER
        subject="Hello Welcome to Email Verification"
        body="This is the last step in the process of Registration with email:"
        #html_messages="<br><font size='3' color='blue'>"+send_email_to+'''</font> <br><a href="'''+{ % url 'index' email_verification_token %}+'''">click here to confirm</a>'''
        html_messages='<br><font size="3" color="blue">'+send_email_to+'</font> <br><a href="http://192.168.17.1:8000/crime_manage/index/'+email_verification_token+'/">click here to confirm</a>'
        result=send_mail(subject,body,from_email,[send_email_to],fail_silently=True,html_message=html_messages)
        print("result"+str(result))
        return result


        

    def send_email_for_password_reset(self,send_email_to,password_otp):
        print(" in send email"+password_otp)
        print("send to email"+send_email_to)
        from_email=settings.EMAIL_HOST_USER
        subject="Hello Welcome to Rest the your Password"
        body="Your one time password is "+password_otp
        result=send_mail(subject,body,from_email,[send_email_to],fail_silently=True)
        print("result"+str(result))
        return result
          

          



    def send_email_for_verification_for_public_users(self,send_email_to, email_verification_token):
        print(" in send email"+email_verification_token)
        print("send to email"+send_email_to)
        from_email=settings.EMAIL_HOST_USER
        subject="Hello Welcome to Email Verification"
        body="This is the last step in the process of Registration with email:"
        html_messages='<br><font size="3" color="blue">'+send_email_to+'</font> <br><a href="http://192.168.17.1:8000/public_users_api/index/'+email_verification_token+'/">click here to confirm</a>'
        print(html_messages)
        result=send_mail(subject,body,from_email,[send_email_to],fail_silently=True,html_message=html_messages)
        print("result"+str(result))
        return result
