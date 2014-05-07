from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.core.context_processors import csrf
from django.template import RequestContext
from userextra.models import ExtendedProfile
from requestreturn.models import Request
from toolmanager.models import Tool

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

def notices(request):
	if request.user.is_authenticated():
		d = dict( notice_list = request.user.extendedprofile.getStackObj() )
		return render_to_response('notices.html', d, context_instance= RequestContext(request))
	else:
		return render_to_response('error.html', {
			"error" : "Insufficient privileges",  # other context 
		}, context_instance = RequestContext(request))


"""
	accept request. remove request from stack, add item to users inventory.
	@param: request (data), id (slugged string)
	@return: actions
"""
def accept(request, key):
	#request is owner
	key = int(key) 
	stack = request.user.extendedprofile.getStack()
	stack.remove(key)
	request.user.extendedprofile.storeStack(stack)
	request.user.extendedprofile.save()

	curr_request = Request.objects.get(id=key)
	curr_request.ownerconfirm = True

	# request model stays archived in DB

	t = curr_request.tool
	d = curr_request.user.extendedprofile.getList() #get target user's inventory.

	if type(d) is dict: # not empty dictionary!

		if curr_request.tool.tool_name in d: #tool already in dictionary
				d[curr_request.tool.tool_name] += 1 #we check out another
		else:
			d[curr_request.tool.tool_name] = 1

	else: #empty dictionary!
		d = {}
		d[curr_request.tool.tool_name] = 1

	# dict -> JSON -> django -> sql3

	curr_request.user.extendedprofile.storeList(d)
	curr_request.user.extendedprofile.save()
	t.checkoutItem()
	t.save()

	return render_to_response('process.html', {
			"transactiontype" : "accepted request",  # other context 
		}, context_instance = RequestContext(request))

"""
	reject request. remove request from stack, do not add item to users inventory.
	@param: request (data), id (slugged string)
	@return: actions
"""
def reject(request, key):
	#request is owner
	key = int(key) 
	stack = request.user.extendedprofile.getStack()
	stack.remove(key)
	request.user.extendedprofile.storeStack(stack)
	request.user.extendedprofile.save()

	curr_request = Request.objects.get(id=key)
	curr_request.ownerconfirm = False # still didnt accept.

	return render_to_response('process.html', {
			"transactiontype" : "accepted rejection",  # other context 
			"extra" : "NOTE: The other party has not been notified to respect your privacy."
		}, context_instance = RequestContext(request))
