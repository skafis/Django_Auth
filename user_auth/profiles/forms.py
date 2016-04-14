from django import forms
from django.utils import timezone
import datetime

from .models import SimplePlace, Skills,  Dated, Create_opportunity, UserSkills

class SingleSkillForm(forms.ModelForm):
	class Meta:
		model = Skills
		fields = [
		'skill'
		]

class PlacedForm(forms.ModelForm):
	class Meta:
		model = SimplePlace
		fields = [
		'location',
		'coordinates',
		'distance_away',
		]
		
class SkillsForm(forms.ModelForm):
	class Meta:
		model = UserSkills
		fields = [
		'skills',
		]
		widgets = {
			'skills': forms.CheckboxSelectMultiple(attrs={'class': 'skillform'}),
		}



class DateForm(forms.ModelForm):
	class Meta:
		model = Dated
		fields = [
		'date',
		'hours'
		]
		widgets = {
		'date': forms.DateInput(attrs={
			'class': 'datepicker'
			})
		}
		
#########################################################################
#frank
class addForm(forms.ModelForm):
    class Meta:
        model = Create_opportunity
        fields = [
        	"image",
            "title",
            "location",
            "coordinates",
            "skills",
            "hours_required",
            "starting_date",
            "stopping_date",
            "description",
        ]
        widgets = {
        	'skills': forms.CheckboxSelectMultiple(attrs={'class': 'skillform'}),
        	'starting_date': forms.DateInput(attrs={'class': 'datepicker'}),
        	'stopping_date': forms.DateInput(attrs={'class':'datepicker'})
        }
        
#############################################################################