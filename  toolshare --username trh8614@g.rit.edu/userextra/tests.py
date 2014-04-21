from django.test import TestCase
from django.contrib.auth.models import User
from userextra.models import ExtendedProfile

"""
forms.py tester for userextra
Author: Bradley Conn

Creates test cases to verify kickbacks from 
the forms.py file. Light to medium testing. 

Includes smoke tests.

"""

class UserExtraTester(TestCase):

	# test setup of zipcode and user profile
	def test_zipcode(self):
		user_info = {'username': 'alice','password': 'swordfish','email': 'alice@example.com'}
	
		u = User.objects.create_user(**user_info)
		random = ExtendedProfile( u, zipcode="12345", inventory="" )
		self.assertEqual(len(random.zipcode), 5)

	# test emptiness of inventory. this cannot be modified by the user!
	def test_get_list(self):
		user_info = {'username': 'alice','password': 'swordfish','email': 'alice@example.com'}
		u = User.objects.create_user(**user_info)
		random = ExtendedProfile( u, zipcode="12345", inventory="" )
		self.assertEqual(random.inventory, "")

	# test if json is working properly with django shorthand keys.
	def test_convert_list(self):
		user_info = {'username': 'alice','password': 'swordfish','email': 'alice@example.com'}
		u = User.objects.create_user(**user_info)
		random = ExtendedProfile( u, zipcode="12345", inventory='["foo", {"bar":["baz", null, 1.0, 2]}]' )
		self.assertEqual(random.getList(), [u'foo', {u'bar': [u'baz', None, 1.0, 2]}])