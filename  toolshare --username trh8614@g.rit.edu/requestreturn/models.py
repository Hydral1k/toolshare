from django.db import models
from django.forms import ModelForm
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db import transaction
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from toolmanager.models import *
from datetime import datetime, date, time
from time import strftime
"""
	Find user in question, do they have stack?

	Yes 
		-> Add to their stack, save.

	No 
		-> Fresh stack, add to user, save.

	@param: user (model object), requestorreturn (model object)
	@return: none

"""



	

"""
	Request created by user. Must be confirmed by owner.
	@param: Model (parameters)
	@return: Model
"""
class Request(models.Model):

	tool = models.ForeignKey(Tool, related_name='Tool',
		error_messages={ 'required' : "You need to select a tool!"})

	owner = models.ForeignKey(User, related_name="owner")
	user = models.ForeignKey(User, related_name="user")

	daterequest = models.DateField( 
		help_text='Please use the following format: <em>YYYY-MM-DD</em>.', 
		default=date.today)

	timerequest = models.TimeField(
		help_text='Please use the following format: <em>HH:HM:SS</em> (24 Hour).',
		default=strftime('%H:%M:%S'))
	datereturn = models.DateField(
		help_text='Please use the following format: <em>YYYY-MM-DD</em>.',
		default=date.today)

	timereturn = models.TimeField(
		help_text='Please use the following format: <em>HH:HM:SS</em> (24 Hour)</em>.',
		default=strftime('%H:%M:%S'))
	
	comment = models.CharField(max_length=300)
	ownerconfirm = models.BooleanField(default=False)

	def __str__(self):
		return "Request"
	
class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['tool', 'owner', 'user', 'daterequest', 'timerequest', 'datereturn', 'timereturn', 'comment']


	
