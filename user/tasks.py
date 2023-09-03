import random
from time import sleep

from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_feedback_email_task(email, otp):
    """Sends an email when the login form has been submitted."""
    sleep(20)
    print(email, otp)
    send_mail("Verify your email", "Your verification code is " + otp +
              "\nDon't share this code!",
              'sanazera2@gmail.com',
              [email], fail_silently=False)
