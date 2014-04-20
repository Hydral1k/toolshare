"""
    SWEN-261
    Tool Share extended user modelbase
"""
from django.db import models
from django.contrib.auth.models import User


"""
    Django extension to user class to add extra DB field to User profiles.
    Uses one to one relationship with ForeignKey.

"""
class Database(models.Model)
    zipcode_dictionary = models.ManyToManyField(self)


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    zipcode = models.CharField(max_length=50, blank=True)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)