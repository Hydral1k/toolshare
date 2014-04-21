from django.test import TestCase
from toolmanager import forms

"""
forms.py tester for toolmanager
Author: Bradley Conn

Creates test cases to verify kickbacks from 
the forms.py file. Light to medium testing. 

Includes smoke tests.

"""

class ToolManagerFormTest(TestCase):

#test name length	
	def test_tool_add_name(self):
		form = forms.ToolForm(data={'tool_name': 'i am going over the one hundred and twenty eight limit of characters, i am going over the one hundred and twenty eight limit of characters',
                                    'tool_manufacture': 'a manufacturue',
                                    'location': '1111',
                                    'tool_description': 'a description',
                        			'quantity': '9',
                                    'quantity_available': '9'})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['tool_name'],
		                 [u"Ensure this value has at most 64 characters (it has 138)."])

#test lmanufacture length
	def test_tool_add_manufacture(self):
		form = forms.ToolForm(data={'tool_name': 'a name',
                                    'tool_manufacture': 'i am going over the one hundred and twenty eight limit of characters, i am going over the one hundred and twenty eight limit of characters',
                                    'location': '1111',
                                    'tool_description': 'a description',
                        			'quantity': '9',
                                    'quantity_available': '9'})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['tool_manufacture'],
		                 [u"Ensure this value has at most 64 characters (it has 138)."])

#test location length
	def test_tool_add_location(self):
		form = forms.ToolForm(data={'tool_name': 'a name',
                                    'tool_manufacture': 'a manufacturue',
                                    'location': 'i am going over the one hundred and twenty eight limit of characters, i am going over the one hundred and twenty eight limit of characters',
                                    'tool_description': 'a description',
                        			'quantity': '9',
                                    'quantity_available': '9'})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['location'],
		                 [u"Ensure this value has at most 32 characters (it has 138)."])

#test description length
	def test_tool_add_description(self):
		form = forms.ToolForm(data={'tool_name': 'a name',
                                    'tool_manufacture': 'a manufacturue',
                                    'location': '1111',
                                    'tool_description': 'i am going over the one hundred and twenty eight limit of characters, i am going over the one hundred and twenty eight limit of characters',
                        			'quantity': '9',
                                    'quantity_available': '9'})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['tool_description'],
		                 [u"Ensure this value has at most 128 characters (it has 138)."])

#test quatity
	def test_tool_add_quantity(self):
		form = forms.ToolForm(data={'tool_name': 'a name',
                                    'tool_manufacture': 'a manufacturue',
                                    'location': '1111',
                                    'tool_description': 'a description',
                        			'quantity': 'not a number',
                                    'quantity_available': '9'})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['quantity'],
		                 [u"A quantity must be entered."])

#test quantity avalailable
	def test_tool_add_quantity_available(self):
		form = forms.ToolForm(data={'tool_name': 'a name',
                                    'tool_manufacture': 'a manufacturue',
                                    'location': '1111',
                                    'tool_Description': 'a description',
                        			'quantity': '9',
                                    'quantity_available': 'not a number'})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['quantity_available'],
		                 [u"A quantity must be entered."])

#test blank space
	def test_tool_add_blank(self):
		form = forms.ToolForm(data={'tool_name': '',
                                    'tool_manufacture': 'a manufacturue',
                                    'location': '1111',
                                    'tool_Description': 'a description',
                        			'quantity': '9',
                                    'quantity_available': '9'})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['tool_name'],
		                 [u"This field is required."])