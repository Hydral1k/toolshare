from django import template
from django.shortcuts import render
from toolmanager.models import *
import math

register = template.Library()


def givemediv(width, tag):
	return "<div style=\"display: table-cell; vertical-align: middle; height: inherit; width: " + str(width) + "px; text-align: center; " + tag +"\">"


"""
finds tool, compares quantity available, total quantity
@parm: toolname (string)
@return: html (html)
"""
@register.filter
def colorfy(toolname):
	print("working")

	t = Tool.objects.get(tool_name__iexact=toolname)
	
	if t == None:
		return "ERROR - Can't find TOOL!" + toolname
	else:
		# parse return
		numerator = t.quantity_available
		denominator = t.quantity
		intensity = math.floor(255*1)

		n = numerator / denominator
		# now we colorfy it.
		r = math.floor(intensity - (intensity*n)) 
		g = math.floor((intensity*n))
		b = 0
		print(r,g,b)
		c = "color: rgb(" + str(r) + "," + str(g) + "," + str(b) +");"
		part1 = givemediv(45, c) + str(numerator) + "</div>"
		part2 = givemediv(10, "color: black;") + "/" + "</div>"
		part3 = givemediv(45, "color: rgb(0, " + str(intensity) + ", 0);" ) + str(denominator) + "</div>"

		return part1 + part2 + part3

		