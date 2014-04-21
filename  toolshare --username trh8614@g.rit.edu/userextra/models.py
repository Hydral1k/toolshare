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
class ExtendedProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    zipcode = models.CharField(max_length=10, blank=True)

   