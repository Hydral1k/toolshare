from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.core.context_processors import csrf
from django.template import RequestContext

"""
	renders index.html
"""
def home(request):
	return render_to_response('index.html', {
		"" : "",  # other context 
	}, context_instance = RequestContext(request))

def profile(request):
	return render_to_response('profile.html', 
		{ "" : ""}, context_instance= RequestContext(request))
