from django.db.models.signals import post_save # post_save is a signal which gets fired after an object is saved i.e. POST method + save() method  [Sender]
from django.contrib.auth.models import User 
from django.dispatch import receiver # receiver is a function which gets the signal and performs some task [Receiver]

from .models import Profile


@receiver(post_save, sender=User) # here we are receiving the post_save signal from User model
def build_profile(sender, instance, created, **kwargs): # here we are defining a function which will be called when a user is created
    if created: # if the user is created then create a profile for that user
        Profile.objects.create(user=instance) # here we are creating a profile for the user

@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs):
    instance.profile.save() # here we are saving the profile of the user


# Path: mysite\users\apps.py here we need to import signals.py