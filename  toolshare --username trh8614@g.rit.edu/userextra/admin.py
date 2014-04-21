from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from userextra.models import ExtendedProfile

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ExtendedProfileInline(admin.StackedInline):
    model = ExtendedProfile
    can_delete = False
    verbose_name_plural = 'extendedprofiles'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ExtendedProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)