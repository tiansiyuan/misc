from django.conf.urls import patterns, include, url
# from django.contrib.auth import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'patient.views.home', name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^register/$', 'patient.views.register'),
    #                   url(r'^login/$', 'login', name='login'),
    # url(r'^logout/$', 'logout'),
    # url(r'^patient/', include('patient.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
