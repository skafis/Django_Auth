from django import forms
from django.utils import timezone
import datetime

from .models import SimplePlace, Skills, Skill, Dated, Create_opportunity

class PlaceForm(forms.ModelForm):
	class Meta:
		model = SimplePlace
		fields = [
		'city',
		'location',
		'skills'
		]
		widgets = {
			'skills': forms.CheckboxSelectMultiple
		}

class PlacedForm(forms.ModelForm):
	class Meta:
		model = SimplePlace
		fields = [
		'city',
		'location',
		'duration',
		]
class SkillsForm(forms.ModelForm):
	class Meta:
		model = SimplePlace
		day = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'id':'datepicker'
                                }))
		fields = [
		'skills',
		]
		widgets = {
			'skills': forms.CheckboxSelectMultiple
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
			'id': 'datepicker'
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
            "skills_needed",
            "hours_required",
            "days",
            "description",
        ]
        
#############################################################################