__author__ = 'vasiliki'

from django.conf.urls import patterns, url

from myapp import views

urlpatterns = patterns('',
    url(r'^home/', views.home, name='home'),
    url(r'^$', views.home, name='home'),
    url(r'^main/', views.main, name='main'),
    url(r'^buildings/', views.buildings, name='buildings'),
    url(r'^street_lighting/', views.street_lighting, name='street_lighting'),
    url(r'^EVs/', views.EVs, name='EVs'),
    url(r'^data_buildings/', views.data_buildings, name='data_buildings'),
    url(r'^data_street_lighting/', views.data_street_lighting, name='data_street_lighting'),
    url(r'^data_EVs/', views.data_EVs, name='data_EVs'),
    url(r'^mydata/', views.mydata, name='mydata'),
    url(r'^data_test/', views.data_test, name='data_test'),
    url(r'^data_main/', views.data_main, name='data_main'),
   # url(r'^data_main_buildings/', views.data_main_buildings, name='data_main_buildings'),
   # url(r'^data_main_street_lighting/', views.data_main_street_lighting, name='data_main_street_lighting'),
   # url(r'^data_main_EVs/', views.data_main_EVs, name='data_main_EVs'),
)