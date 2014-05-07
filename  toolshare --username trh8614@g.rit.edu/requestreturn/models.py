from django.db import models
from django.forms import ModelForm
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db import transaction
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from userextra.models import ExtendedProfile
from toolmanager.models import *
"""
	Find user in question, do they have stack?

	Yes 
		-> Add to their stack, save.

	No 
		-> Fresh stack, add to user, save.

	@param: user (model object), requestorreturn (model object)
	@return: none

"""

def StackFactory( user, requestorreturn):

	u = User.objects.get(user)

	# this user has nothing in his stack
	# let's add to his collection!
	if u.extendedprofile.emptyStack():

		stack = []
		stack.append(requestorreturn)

		u.extendedprofile.storeStack(stack)
		u.extendedprofile.save()

	# user has items in his stack
	# let's accomidate to his pile and add request to top.
	else: 

		stack = u.extendedprofile.getStack()
		stack.append(requestorreturn)

		u.extendedprofile.storeStack(stack)
		u.extendedprofile.save()

	

"""
	Request created by user. Must be confirmed by owner.
	@param: Model (parameters)
	@return: Model
"""
class Request(models.Model):

	tool = models.ManyToManyField(Tool)

	owner = models.ForeignKey(User, related_name="owner")
	user = models.ForeignKey(User, related_name="user")

	daterequest = models.DateField(
		help_text='Please use the following format: <em>YYYY-MM-DD</em>.')
	timerequest = models.TimeField(
		help_text='Please use the following format: <em>HH-MM</em>.')
	datereturn = models.DateField(
		help_text='Please use the following format: <em>YYYY-MM-DD</em>.')
	timereturn = models.TimeField(
		help_text='Please use the following format: <em>HH-MM</em>.')
	
	comment = models.CharField(max_length=300)
	ownerconfirm = models.BooleanField()
	
class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['tool', 'owner', 'user', 'daterequest', 'timerequest', 'datereturn', 'timereturn']
