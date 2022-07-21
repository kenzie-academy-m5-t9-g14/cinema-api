from django.core.mail import send_mail



def sendEmail(subject,message,from_email,recipient_list):
  send_mail(subject = subject,
     message = message,
     from_email = from_email,
     recipient_list = recipient_list,
     fail_silently = False)