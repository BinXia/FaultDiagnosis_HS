from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FaultDiagnosis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('Homepage.urls', namespace="Homepage")),

)
