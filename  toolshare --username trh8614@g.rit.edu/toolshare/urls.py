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
    url(r'^notices/', 'toolshare.views.notices'),
    url(r'^accounts/profile', 'toolshare.views.profile'),
    url(r'^tools/browse/', 'toolmanager.views.browse'),
    url(r'^tools/add/', 'toolmanager.views.add'),
    url(r'^tools/view/(?P<tool>[a-zA-Z0-9_.-]+)', 'toolmanager.views.describeItem'),
    url(r'^tools/addone/(?P<tool>[a-zA-Z0-9_.-]+)/$', 'toolmanager.views.addOne'),
    url(r'^tools/minusone/(?P<tool>[a-zA-Z0-9_.-]+)/$', 'toolmanager.views.minusOne'),
    url(r'^tools/checkout/(?P<tool>[a-zA-Z0-9_.-]+)/$', 'toolmanager.views.checkoutItem'),
    url(r'^tools/return/(?P<tool>[a-zA-Z0-9_.-]+)/$', 'toolmanager.views.returnItem'),
    url(r'^tools/accept/(?P<key>[0-9_.-]+)', 'toolshare.views.accept'),
    url(r'^tools/reject/(?P<key>[0-9_.-]+)', 'toolshare.views.reject'),
    url(r'^tools/', 'toolmanager.views.browse')


    
)
urlpatterns += staticfiles_urlpatterns()