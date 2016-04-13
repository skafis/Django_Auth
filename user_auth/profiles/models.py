from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.conf import settings

# Kiilus imports
from django.core.urlresolvers import reverse
from location_field.models.plain import PlainLocationField

# Create your models here.
# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length = 1200)
	description = models.TextField(default = 'description default')
	
	def __unicode__(self):
		return self.name
		
		
		
class Opportunity(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
	title = models.CharField(max_length=120)
	image = models.ImageField(null=True, blank=True)
	description = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	
	def __str__(self):
		return self.title


	def __unicode__(self):
		return self.title
#===============================================
# Kiilu
class Skills(models.Model):
    skill = models.CharField(max_length=255)
    def __unicode__(self):
        return self.skill

class SimplePlace(models.Model):
    user =  models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    duration = models.IntegerField(default=0)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    skills = models.ManyToManyField(Skills)

    def __unicode__(self):
    	return self.city

    def get_absolute_url(self):
		return reverse("page", kwargs={"id": self.id})

class Skill(models.Model):
    skill = models.ManyToManyField(SimplePlace)


class Dated(models.Model):
    user =  models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    hours = models.IntegerField(default=0)
#=======================================================

#########################################################
#frank
# models for creating opportunity
class Create_opportunity(models.Model):
    image = models.ImageField(upload_to='static/image', verbose_name='My Photo', blank = True, default = 0)
    title = models.CharField(max_length=140)
    location = models.CharField(max_length=140)
    description = models.TextField(null=True)
    skills_needed = models.CharField(max_length=140, blank = True)
    hours_required = models.CharField(max_length=140, blank = True)
    days = models.CharField(max_length=140, blank = True)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title