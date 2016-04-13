from django.conf.urls import patterns, url, include
from django.contrib import admin
from profiles import views

admin.autodiscover()



urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^usertype/$', views.usertype),
        url(r'^helper/$', views.helper),
        url(r'^seeker/$', views.seeker),
        url(r'^location/$', views.location, name='location'),
        url(r'^skills/$', views.skills, name='skills'),
        url(r'^days/$', views.days, name='days'),
        url(r'^create/$', views.create_opportunity_form, name = "create"),
        )