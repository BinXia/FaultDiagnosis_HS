from django.conf.urls import patterns, url
from Status import views

urlpatterns = patterns('',
    url(r'^Dynamic', views.UpdataDynamicData, name='UpdataDynamicData'),
    url(r'^Search', views.SearchForHistory, name='SearchForHistory'),
    url(r'^HistoryRecord', views.RecordForHistory, name='RecordForHistory'),

)