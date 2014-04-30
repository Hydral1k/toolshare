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
    INVENTORY_LIMIT = 999999
    user = models.OneToOneField(User, unique=True)
    zipcode = models.CharField(max_length=10, blank=True)
    inventory = models.CharField(max_length=INVENTORY_LIMIT, editable=False) #dataslot for json!

    """
        storeList
        
        Stores a data set (anytype, but in this application a dictionary) into 
        the MySQL database field related to the user.
        
        @param: self-object (relation related), data-dict (list of items in user
        inventory)
        @return: false if error.
    """
    def storeList( self, data ):
        d = json.dumps(data)
        if len(d) > INVENTORY_LIMIT :
            raise Exception("Current user inventory data over MySQL field limit. Increase limit constant")
            return False
        else:
            self.inventory = d
            
    """
        getList
        
        Retrieves mySQL self.inventory field
        
        @param: self-object (relation related)
        @return: dict object (inventory list)
    """
    def getList( self ):
        if self.inventory == "": #no data, fresh inventory.
            return ""
        else:
            return json.loads(self.inventory)

    REQUIRED_FIELDS = ['zipcode']

   