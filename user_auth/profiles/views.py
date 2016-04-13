from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from urllib import quote_plus
from django.contrib import messages

from .models import Opportunity

# Kiilu imports
# Rendering views
from .models import SimplePlace
from .forms import PlaceForm, PlacedForm, SkillsForm, DateForm

from django.utils import timezone

# Math class
import math

from django.db.models import Q


# Create your views here.
def index(request):
	context = {}
	template = 'profiles/index.html'
	return render(request, template, context)
	
def usertype(request):
	context = {}
	template = 'profiles/usertype.html'
	return render(request, template, context)

def seeker(request):
	context = {}
	template = 'profiles/seekerProfile.html'
	return render(request, template, context)
	

def helper(request):
	context = {}
	template = 'profiles/helperProfile.html'
	return render(request, template, context)
	
	
def browseOpportunity(request):
	context = {}
	template = 'profiles/helperProfile.html'
	return render(request, template, context)	
	
	
# def post_list(request):
# 	today = timezone.now().date()
# 	queryset_list = Post.objects.active()#.order_by("-timestamp")
# 	if request.user.is_staff or request.user.is_superuser:
# 		queryset_list = Post.objects.all()

# 	query = request.GET.get("q")
# 	if query:
# 		queryset_list = queryset_list.filter(title__icontains=query)

# 	paginator = Paginator(queryset_list, 5) # Show 5 contacts per page
# 	page_request_var = "abc"
# 	page = request.GET.get(page_request_var)
# 	try:
# 		queryset = paginator.page(page)
# 	except PageNotAnInteger:
# 	# If page is not an integer, deliver first page.
# 		queryset = paginator.page(1)
# 	except EmptyPage:
# 	# If page is out of range (e.g. 9999), deliver last page of results.
# 		queryset = paginator.page(paginator.num_pages)

# 	context = {
# 		"object_list": queryset,
# 		"title": "List",
# 		"page_request_var": page_request_var,
# 		"today": today,
# 		}
		
# 	return render(request, "post_list.html", context)	

def location(request):
	# Location page view
	form = PlacedForm(data = request.POST)
	nearby_places = []
	other_places = SimplePlace.objects.values('location', 'city')
	
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		
		for place in other_places:
			if place['location'].split(",") != ['']:
				lat = float(place['location'].split(",")[0])
				lng = float(place['location'].split(",")[1])
				current_lat = float(instance.location.split(",")[0])
				current_lng = float(instance.location.split(",")[1])
				
				# Calculate places within a certain distance
				distance = calc_dist(current_lat, current_lng, lat, lng)
		
				if distance < 50.0 and instance.city != place['city']:
					nearby_places.append(place)


		# Remove duplicates
		nearby_places = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in nearby_places)]

	

	context = {
		'other_places':nearby_places,	
		'form':form,
	}
	return render(request, "project/location.html", context)
	
def skills(request):
	form = SkillsForm(data = request.POST)	
	query = request.GET.get("q")
	if query:
		form.fields['skills'].queryset = form.fields['skills'].queryset.filter(Q(skill__icontains=query))
		
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user =request.user
		instance.save()


	context = {
		"form": form,
	}
	return render(request, "project/skills.html", context)

def days(request):
	date = DateForm(data = request.POST)
	if date.is_valid():
		instance = date.save(commit=False)
		instance.user = request.user
		instance.save()
	context = {
		'date': date,
	}
	return render(request, "project/days.html", context)
	
def calc_dist(lat1, lon1, lat2, lon2):
	'''a function to calculate the distance in miles between two 
	points on the earth, given their latitudes and longitudes in degrees'''


	# covert degrees to radians
	lat1 = math.radians(lat1)
	lon1 = math.radians(lon1)
	lat2 = math.radians(lat2)
	lon2 = math.radians(lon2) 

	# get the differences
	delta_lat = lat2 - lat1 
	delta_lon = lon2 - lon1 

	# Haversine formula, 
	# from http://www.movable-type.co.uk/scripts/latlong.html
	a = ((math.sin(delta_lat/2))**2) + math.cos(lat1)*math.cos(lat2)*((math.sin(delta_lon/2))**2) 
	c = 2 * math.atan2(a**0.5, (1-a)**0.5)
	# earth's radius in km
	earth_radius = 6371
	# return distance in miles
	return earth_radius * c