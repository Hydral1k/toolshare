from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.core.context_processors import csrf
from django.template import RequestContext
# Create your views here.

def home(request):
	return render_to_response('tools/index.html', {
		"" : "",  # other context 
	}, context_instance = RequestContext(request))

def browse(request):
	return render_to_response('tools/browse.html', {
		"" : "",  # other context 
	}, context_instance = RequestContext(request))