from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'toolshare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/', 'toolshare.views.registration'),
    url(r'^$', 'toolshare.views.home'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
urlpatterns += staticfiles_urlpatterns()