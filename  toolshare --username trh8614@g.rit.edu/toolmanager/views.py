from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.core.context_processors import csrf
from django.forms import ModelForm
from django.template import RequestContext
from toolmanager.models import Tool
from django.forms.models import modelformset_factory

# Create your views here.

class AddForm(ModelForm):
	class Meta:
		model = Tool
		fields = ['tool_name', 'tool_manufacture', 'location', 'tool_description', 'quantity', 'quantity_available']

def home(request):
	return render_to_response('tools/index.html', {
		"" : "",  # other context 
	}, context_instance = RequestContext(request))

def browse(request):
	d = dict( tool_list = Tool.objects.all() )
	return render_to_response('tools/browse.html', d, context_instance = RequestContext(request))

def add(request):

	form = AddForm()
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():
			form.save()
			d = dict( tool_list = Tool.objects.all() )
			return render_to_response('tools/browse.html', d, context_instance = RequestContext(request))
	else:
		form = AddForm()

	return render_to_response('tools/add.html', {"form":form}, context_instance = RequestContext(request))


