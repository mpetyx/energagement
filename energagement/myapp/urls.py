__author__ = 'vasiliki'

from django.conf.urls import patterns, url

from myapp import views

urlpatterns = patterns('',
    url(r'^main/', views.main, name='main'),
)