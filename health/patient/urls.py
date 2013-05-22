from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'list', 'patient.views.list'),
                       url(r'edit_profile', 'patient.views.edit_profile'),
)
