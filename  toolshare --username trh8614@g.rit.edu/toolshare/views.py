from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.core.context_processors import csrf
from django.template import RequestContext
def home(request):
	 # ...
    return render_to_response('index.html', {
        "na" : "na",  # other context 
    }, context_instance = RequestContext(request))
