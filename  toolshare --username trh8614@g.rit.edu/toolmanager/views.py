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
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.core.context_processors import csrf
from django.forms import ModelForm
from django.template import RequestContext
from toolmanager.models import Tool
from toolmanager.forms import ToolForm
from django.forms.models import modelformset_factory


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
	d = dict( tool_list = Tool.objects.all() )
	return render_to_response('tools/browse.html', d, context_instance = RequestContext(request))

"""
# Add view. Used to to render form which allows used to add a tool
# to the master database. This method cycles twice for when a tool is added.
# Dependent of AddForm meta class.
# 
# param: request (DJANGO PAGE REQUEST)
# return: page render with context (form context OR  with tool library dictionary )
"""
def add(request):

	form = ToolForm()
	if request.method == 'POST': #looks like the user is trying to save a new tool!
		form = ToolForm(request.POST)
		if form.is_valid():
			form.save()
			d = dict( tool_list = Tool.objects.all() )
			return render_to_response('tools/browse.html', d, context_instance = RequestContext(request))
	else: #let's just create the new form for the user.
		form = ToolForm()

	return render_to_response('tools/add.html', {"form":form}, context_instance = RequestContext(request))


