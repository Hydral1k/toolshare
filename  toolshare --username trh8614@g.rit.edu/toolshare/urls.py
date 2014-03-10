from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^accounts/', include('registration.backends.default.urls')),
    # Examples:
    # url(r'^$', 'toolshare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'toolshare.views.home'),
    url(r'^accounts/profile', 'toolshare.views.profile'),
    url(r'^tools/', 'toolmanager.views.home')
    
)
urlpatterns += staticfiles_urlpatterns()