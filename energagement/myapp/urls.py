__author__ = 'vasiliki'

from django.conf.urls import patterns, url

from myapp import views

urlpatterns = patterns('',
    url(r'^home/', views.home, name='home'),
    url(r'^$', views.home, name='home'),
    url(r'^main/', views.main, name='main'),
    url(r'^buildings/', views.buildings, name='buildings'),
    url(r'^street_lighting/', views.street_lighting, name='street_lighting'),
    url(r'^EV/', views.EV, name='EV'),
    url(r'^test/', views.test, name='test'),
    #url(r'^test2/', views.test2, name='test2'),
    url(r'^mydata/', views.mydata, name='mydata'),
    url(r'^data_test/', views.data_test, name='data_test'),
)