from django.conf.urls import patterns, url
from Homepage import views

urlpatterns = patterns('',
    
    url(r'^admin/$', views.index, name='index'),

)