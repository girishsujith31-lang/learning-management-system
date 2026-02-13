from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Automatically create a profile when a user is created."""
    if created:
        # Only create if role is provided in POST data, otherwise default to student
        Profile.objects.get_or_create(user=instance, defaults={'role': 'student'})


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save the profile when user is saved."""
    if hasattr(instance, 'profile'):
        instance.profile.save()
