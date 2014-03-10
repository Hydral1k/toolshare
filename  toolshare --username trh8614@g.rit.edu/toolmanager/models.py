from django.db import models
from django.contrib import admin

class Tool(models.Model):
	tool_name = models.CharField(max_length=128)
	tool_manufacture = models.CharField(max_length=128)
	location = models.CharField(max_length=128)
	tool_description = models.TextField()
	quantity = models.IntegerField()
	quantity_available = models.IntegerField()
	
class AdminTools(admin.ModelAdmin):
	search_fields = ["tool_name"]
	display_fields = ["tool_name", "quantity_available"]


