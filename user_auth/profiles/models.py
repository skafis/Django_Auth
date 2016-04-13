from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.conf import settings

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