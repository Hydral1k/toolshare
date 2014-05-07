from django.shortcuts import render
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
from django.forms.models import modelformset_factory
from django.contrib.auth import get_user_model

# Create your views here.
