from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save


class Profile(models.Model):
    """
    Model for user profile
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image', default='placeholder')        
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def create_profile(instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


def create_profile(instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)


class Photo(models.Model):
    image = CloudinaryField('image')