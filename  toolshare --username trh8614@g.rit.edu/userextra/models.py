"""
    SWEN-261
    Tool Share extended user modelbase

    Thomas Heissenberger
"""
from django.db import models
from django.contrib.auth.models import User
import json # we use this to package to sql3


"""
    Django extension to user class to add extra DB field to User profiles.
    Uses one to one relationship with ForeignKey.

"""
class ExtendedProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    zipcode = models.CharField(max_length=10, blank=True)
    inventory = models.CharField(max_length=999999) #dataslot for json!

    def storeList( data ):
    	self.inventory = json.dumps(data)

    def getList( data ):
    	return json.loads(self.inventory)

   