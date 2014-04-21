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
	if request.user.is_authenticated():
		d = dict( inventory = request.user.extendedprofile.getList() )
		return render_to_response('profile.html', d, context_instance= RequestContext(request))
	else:
		return render_to_response('error.html', {
			"error" : "Insufficient privileges",  # other context 
		}, context_instance = RequestContext(request))
