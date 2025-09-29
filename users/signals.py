"""from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()"""
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Profile


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()



import random
import string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from allauth.account.signals import user_signed_up
from .models import Profile

def generate_random_password(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(user_signed_up)
def send_welcome_email(request, user, **kwargs):
    try:
        # Generate a random password
        random_password = generate_random_password()
        
        # Set the user's password
        user.set_password(random_password)
        user.save()
        
        subject = "Welcome to GenAI"
        
        html_message = render_to_string('email/welcome_email.html', {
            'user': user,
            'password': random_password,
            'expiry': timezone.now() + timezone.timedelta(minutes=30)
        })
        plain_message = strip_tags(html_message)
        
        message = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email]
        )
        message.attach_alternative(html_message, "text/html")
        message.send()
    except Exception as e:
        print(f"Error: {e}")  # Debug statement
        pass  # Handle the exception as needed