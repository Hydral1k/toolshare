"""
    Toolshare Form

    Thomas Heissenberger

"""

from django import forms
from django.utils.translation import ugettext_lazy as _
from toolmanager.models import Tool
from django.core.validators import MinValueValidator, MaxValueValidator



"""
    A tool form for adding a tool which can be rendered through HTML.

"""
class ToolForm( forms.Form ):

    fields = ['tool_name', 'tool_manufacture', 'location', 'tool_description', 'quantity', 'quantity_available']

    tool_name = forms.CharField(max_length=64,
                                label=_("Tool Name"),
                                error_messages={'invalid': _("Your input is too long.")})

    tool_manufacture = forms.CharField(max_length=64,
                                label=_("Tool Manufacture"),
                                error_messages={'invalid': _("Your input is too long.")})

    location = forms.CharField(max_length=32,
                                label=_("Location"),
                                error_messages={'invalid': _("Your input is too long.")})


    tool_description = forms.CharField(max_length=128,
                                label=_("Description"),
                                error_messages={'invalid': _("Your input is too long.")})

    quantity = forms.IntegerField(required=True, error_messages={'invalid': _("Your input is too long.")})

    quantity_available = forms.IntegerField(error_messages={'invalid': _("A quantity must be entered.")},
                                   label = _("Quantity Available"),
                                   required=True)
