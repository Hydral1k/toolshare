from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db import transaction
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from userextra.models import ExtendedProfile
from toolmanager.models import *

class RequestFactory():

	


"""
	Request created by user. Must be confirmed by owner.
"""
class Request(models.Manager):

	daterequest = models.DateField(
		auto_now_add=True,
		help_text='Please use the following format: <em>YYYY-MM-DD</em>.',
		error_message='Please enter a valid date!'
		)
	timerequest = models.TimeField(
		auto_now_add=True,
		help_text='Please use the following format: <em>HH-MM</em>.',
		error_message='Please enter a valid time!')
	datereturn = models.DateField(
		auto_now_add=True,
		help_text='Please use the following format: <em>YYYY-MM-DD</em>.',
		error_message='Please enter a valid date!')
	timereturn = models.TimeField(
		auto_now_add=True,
		help_text='Please use the following format: <em>HH-MM</em>.',
		error_message='Please enter a valid time!')
	tool = None
	comment = models.CharField(max_length=300)
	ownerconfirm = models.BooleanField()
	lengthusage = "" # will be determined by timerequest-timereturn