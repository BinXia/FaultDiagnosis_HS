from django.conf.urls import patterns, url
from Status import views

urlpatterns = patterns('',
    
    url(r'^$', views.health(), name='health'),

)