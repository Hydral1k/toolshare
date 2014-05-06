"""
SWEN-261 toolshare
Group 1 'The D is Silent'

Master models page for tool object / class

	Thomas Heissenberger
	Eric Tevelson
"""
from django.db import models
from django.contrib import admin
from django.utils.text import slugify
from django.contrib.auth.models import User
"""
	Using Django Database class style. 
	Configures database to save Tool objects, with specific attributes listed below
	@param : none
	@return: none
"""
class Tool(models.Model):
	tool_name = models.CharField(max_length=128)
	tool_manufacture = models.CharField(max_length=128)
	location = models.CharField(max_length=128)
	tool_description = models.TextField()
	quantity = models.IntegerField()
	quantity_available = models.IntegerField()
	# create a relation of the tool to the user,
	owner = models.ForeignKey(User, related_name="wat")

	# admin only methods.
	def addquant(self):
		self.quantity=self.quantity+1
		self.quantity_available=self.quantity_available+1
	def subquant(self):
		self.quantity=self.quantity-1
		self.quantity_available=self.quantity_available-1

	# user methods.
	def checkoutItem(self):
		self.quantity_available = min(self.quantity, max(0, self.quantity_available - 1))

	def returnItem(self):
		self.quantity_available = min(self.quantity, max(0, self.quantity_available + 1))

	# slug up the name
	# MAY BE SCRAPPED R2 REFACTOR
	def getimgname():
		return slugify(self.tool_name.lower())
			


"""
	Configures Django admin class to enable search for tool_name field.
"""
class AdminTools(admin.ModelAdmin):
	search_fields = ["tool_name"]
	display_fields = ["tool_name", "quantity_available"]


