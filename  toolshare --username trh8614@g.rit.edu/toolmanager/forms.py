"""
    Toolshare Form

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

    fields[0] = forms.CharField(max_length=64,
                                label=_("Tool Name"),
                                error_messages={'invalid': _("Your input is too long.")})

    fields[1] = forms.CharField(max_length=64,
                                label=_("Tool Manufacture"),
                                error_messages={'invalid': _("Your input is too long.")})

    fields[2] = forms.CharField(max_length=32,
                                label=_("Location"),
                                error_messages={'invalid': _("Your input is too long.")})


    fields[3] = forms.CharField(max_length=128,
                                label=_("Description"),
                                error_messages={'invalid': _("Your input is too long.")})

    fields[4] = forms.IntegerField()

    fields[5] = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(int(fields[4]))], 
                                   error_messages={'invalid': _("Your value is to above the Total Quantity or below 0")},
                                   label = _("Quantity Available"))
