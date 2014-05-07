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
    INVENTORY_LIMIT = 99999
    STACK_LIMIT = 99999
    user = models.OneToOneField(User, unique=True)
    zipcode = models.CharField(max_length=10, blank=True)
    inventory = models.CharField(max_length=INVENTORY_LIMIT, editable=False) #dataslot for json!
    stack = models.CharField(max_length=INVENTORY_LIMIT, editable=False) #dataslot for json!
    stacksize = models.CharField(max_length=INVENTORY_LIMIT, editable=False, default=0) #dataslot for json!

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
        if len(d) > self.INVENTORY_LIMIT :
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

    # as above, except for stack
    def storeStack( self, data):
        d = json.dumps(data)
        if len(d) > self.STACK_LIMIT :
            raise Exception("Current user stack data over MySQL field limit. Increase limit constant")
            return False
        else:
            self.stack = d
            print(self.stack)
            print("fucksalt")
            self.stacksize = len(data)
    # as above, except for stack
    def getStack( self ):
        if self.stack == "": #no data, fresh stack.
            return ""
        else:
            return json.loads(self.stack)

    def emptyStack( self ):
        if self.stack == "": #no data, fresh stack.
            return True

    REQUIRED_FIELDS = ['zipcode']

   
