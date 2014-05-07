"""
SWEN 261
toolshare
Group 1 'The D is Silent'
Thomas Heissenberger - 4/9/2014

views.py 

Controls web views via urls.py file. Also used to redirect and pipeline proper
data and context. Currently in light state.
"""


from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.core.context_processors import csrf
from django.forms import ModelForm
from django.template import RequestContext
from toolmanager.models import Tool
from toolmanager.forms import ToolForm
from requestreturn.models import Request, RequestForm
from django.forms.models import modelformset_factory
from django.forms.models import modelform_factory
from django.contrib.auth import get_user_model



def home(request):
	return render_to_response('tools/index.html', {
		"" : "",  # other context 
	}, context_instance = RequestContext(request))

"""
# Browse view. Used to browse tools which is rendered in list style
# 
# param: request (DJANGO PAGE REQUEST)
# return: page render with context (Tool object dictionary )
"""
def browse(request):
	if request.user.is_authenticated():
		d = dict( tool_list = Tool.objects.all() )
		for tools in d['tool_list']: 
			print(tools)
		
			if tools.tool_name in request.user.extendedprofile.getList():

				tools.canReturn = True
			# let's find tools that are in our inventory.

		return render_to_response('tools/browse.html', d, context_instance = RequestContext(request))
	else:
		return render_to_response('error.html', {"error" : "Insufficient privileges"}, context_instance = RequestContext(request))

"""
# Add view. Used to to render form which allows used to add a tool
# to the master database. This method cycles twice for when a tool is added.
# Dependent of AddForm meta class.
# 
# param: request (DJANGO PAGE REQUEST)
# return: page render with context (form context OR  with tool library dictionary )
"""
def add(request):
	if request.user.is_authenticated():

		form = ToolForm()
		if request.method == 'POST': #looks like the user is trying to save a new tool!
			form = ToolForm(request.POST)
			if form.is_valid():
				if Tool.objects.filter(tool_name=form.cleaned_data["tool_name"]).exists():
					return render_to_response('error.html', {
						"error" : "Duplicates detected in the database! Please only add one!",  # other context 
					}, context_instance = RequestContext(request))

				tool = Tool( tool_name=form.cleaned_data["tool_name"], tool_manufacture=form.cleaned_data["tool_manufacture"], location=form.cleaned_data["location"], tool_description=form.cleaned_data["tool_description"], quantity=form.cleaned_data["quantity"],
							 quantity_available=max(min(form.cleaned_data["quantity_available"], form.cleaned_data["quantity"]), 0), owner=request.user)
				tool.save()
				d = dict( tool_list = Tool.objects.all() )
				return redirect('toolmanager.browse')
		else: #let's just create the new form for the user.
			form = ToolForm()

		return render_to_response('tools/add.html', {"form":form}, context_instance = RequestContext(request))
	else:
		return render_to_response('error.html', {
					"error" : "Insufficient privileges",  # other context 
				}, context_instance = RequestContext(request))

"""
# Checks out item. Called via url dispatcher.
#
# @param request-data, tool-string
# @return Commits change to tool object, reducing quantity and
# adding value to respective user inventory.
# Then redirects to browser page. Requires membership
#
"""

### WARNING!
### Request is a form object.
### request is a native object to Django web queries!
###
### THEY ARE NOT THE SAME!
def checkoutItem(request, tool):
	unslug = tool.replace('-', ' ')
	t  = Tool.objects.get(tool_name__iexact=unslug)

	if t.quantity_available == 0:

		return render_to_response('error.html', {
			"error" : "Out of stock!",  # other context 
		}, context_instance = RequestContext(request))

	elif request.user.is_authenticated() :

		#let's fetch their json list.
		d = request.user.extendedprofile.getList()

		# now we create a request
		request_form = RequestForm(instance = t)
		

		if request.method == 'POST':
			form = request_form(request.POST)
			form.save()

		else:
			return render_to_response('tools/request.html', {"form":request_form}, context_instance = RequestContext(request))


		
		if type(d) is dict: # not empty dictionary!

			if t.tool_name in d: #tool already in dictionary
				d[t.tool_name] += 1 #we check out another
			else:
				d[t.tool_name] = 1

		else: #empty dictionary!
			d = {}
			d[t.tool_name] = 1

		# dict -> JSON -> django -> sql3

		request.user.extendedprofile.storeList(d)
		request.user.extendedprofile.save()
		t.checkoutItem()
		t.save()

		d = dict( tool_list = Tool.objects.all() )
		return redirect('toolmanager.browse')
	
	else:
		return render_to_response('error.html', {
			"error" : "Insufficient privileges",  # other context 
		}, context_instance = RequestContext(request))

"""
# Returns item. Called via url dispatcher.
#
# @param request-data, tool-string
# @return Commits change to tool object, adding quantity and
# removing value from respective user inventory.
# Then redirects to browser page. Requires membership
#
"""
def returnItem(request, tool):
	if request.user.is_authenticated():
		unslug = tool.replace('-', ' ')
		t  = Tool.objects.get(tool_name__iexact=unslug)
		#let's fetch their json list.
		d = request.user.extendedprofile.getList()
		if type(d) is dict: # not empty dictionary!
			if t.tool_name in d: #tool already in dictionary
				if d[t.tool_name] > 1:
					print("removin")
					d[t.tool_name] = d[t.tool_name] - 1
				else:
					print("poppin")
					d.pop(t.tool_name, None)

		else: #empty dictionary!
			return render_to_response('error.html', {
			"error" : "Django issue with return view. Please report.",  # other context 
		}, context_instance = RequestContext(request))

		# dict -> JSON -> django -> sql3

		request.user.extendedprofile.storeList(d)
		request.user.extendedprofile.save()
		t.returnItem()
		t.save()

		d = dict( tool_list = Tool.objects.all() )
		return redirect('toolmanager.browse')
	
	else:
		return render_to_response('error.html', {
			"error" : "Insufficient privileges",  # other context 
		}, context_instance = RequestContext(request))

"""
	describeItem

	Shows info and describes the item. Essentially an info page.
	@param: request (preinfo), tool (slugged string, name)
	@return: renders tool page.

"""
def describeItem(request, tool):
	
	# we fetch the tool
	unslug = tool.replace('-', ' ')
	t  = Tool.objects.get(tool_name__iexact=unslug)
	d = dict( tool = t )

	return render_to_response('tools/tool.html', d, context_instance = RequestContext(request))


def addOne(request, tool):

	if not (request.user.is_staff or request.user.is_superuser):

		return render_to_response('error.html', {
			"error" : "You need Admin privaleges!",  # other context 
		}, context_instance = RequestContext(request))

	else:

		unslug = tool.replace('-', ' ')
		t  = Tool.objects.get(tool_name__iexact=unslug)

		if t:
			t.addquant()
			t.save()

		return redirect('toolmanager.browse')

def minusOne(request, tool):

	if not (request.user.is_staff or request.user.is_superuser):

		return render_to_response('error.html', {
			"error" : "You need Admin privaleges!",  # other context 
		}, context_instance = RequestContext(request))

	else:
		unslug = tool.replace('-', ' ')
		t  = Tool.objects.get(tool_name__iexact=unslug)

		if t:
			t.subquant()
			t.save()

		return redirect('toolmanager.browse')


