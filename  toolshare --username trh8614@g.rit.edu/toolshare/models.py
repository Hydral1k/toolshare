"""
	SWEN-261
	Tool Share extended user modelbase
"""
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import json


"""
	Django extension to user class to add extra DB field to User profiles.
	Uses one to one relationship with ForeignKey.

"""
class Database(models.Model)
	zipcode_dictionary = models.ManyToManyField(self)


class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	zipcode = models.IntegerField(max_length=10, blank=True)

	# make user object print out in a pretty fashion
	def __str__(self):
		return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
	if created:
			profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

