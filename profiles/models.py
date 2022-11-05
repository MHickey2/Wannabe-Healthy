from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class Profile(models.Model):
    """
    Model for user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = CloudinaryField('image', default='placeholder')   
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'


# @receiver(post_save, user)
# def create_or_update_user_profile(user, instance, created, **kwargs):
#     """
#     Create or update the user profile
#     """
#     if created:
#         UserProfile.objects.create(user=instance)
#     # Existing users: just save the profile
#     instance.userprofile.save()
    