"""
SWEN-261 toolshare
Group 1 'The D is Silent'

Master models page for tool object / class
"""
from django.db import models
from django.contrib import admin
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

	def addquant():
		quantity=quantity+1;

	def  subquant():
		quantity=quantity-1;

"""
	Configures Django admin class to enable search for tool_name field.
"""
class AdminTools(admin.ModelAdmin):
	search_fields = ["tool_name"]
	display_fields = ["tool_name", "quantity_available"]


