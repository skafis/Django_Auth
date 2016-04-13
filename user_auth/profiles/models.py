from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.conf import settings

# Kiilus imports
from django.core.urlresolvers import reverse
from django.db import models as pmodels
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
		
class Skills(pmodels.Model):
    skill = pmodels.CharField(max_length=255)
    def __unicode__(self):
        return self.skill

class SimplePlace(pmodels.Model):
    user =  pmodels.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    duration = pmodels.IntegerField(default=0)
    city = pmodels.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    skills = pmodels.ManyToManyField(Skills)

    def __unicode__(self):
    	return self.city

    def get_absolute_url(self):
		return reverse("page", kwargs={"id": self.id})

class Skill(pmodels.Model):
    skill = pmodels.ManyToManyField(SimplePlace)


class Dated(pmodels.Model):
    user =  pmodels.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = pmodels.DateTimeField()
    hours = pmodels.IntegerField(default=0)