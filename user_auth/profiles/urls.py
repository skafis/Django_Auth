from django.conf.urls import patterns, url, include
from django.contrib import admin
from profiles import views

admin.autodiscover()



urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^usertype/$', views.usertype),
        url(r'^helper/$', views.helper),
        url(r'^seeker/$', views.seeker),
        )