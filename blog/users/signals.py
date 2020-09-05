"""Signals"""
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Create a profile whenever a user is registered

    How this works:
        When a User is saved we call post_save (the signal) and it is
        received by the `create_profile` function.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Save the profile when the user is saved.
    """
    instance.profile.save()
