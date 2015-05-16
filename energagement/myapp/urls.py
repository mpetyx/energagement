__author__ = 'vasiliki'

from django.conf.urls import patterns, url

from myapp import views

urlpatterns = patterns('',
    url(r'^main/', views.main, name='main'),
    url(r'^buildings/', views.buildings, name='buildings'),
    url(r'^street_lighting/', views.street_lighting, name='street_lighting'),
    url(r'^EV/', views.EV, name='EV'),
)