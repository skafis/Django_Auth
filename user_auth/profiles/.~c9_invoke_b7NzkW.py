from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from urllib import quote_plus
from django.contrib import messages



# Kiilu imports
# Rendering views
from .models import SimplePlace, Create_opportunity
from .forms import SingleSkillForm, PlacedForm, SkillsForm, DateForm, addForm
from datetime import timedelta

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
#############################################################################
# Chris Kiilu
def location(request):
	# coordinates page view
	form = PlacedForm(data = request.POST)
	nearby_places = []
	other_places = SimplePlace.objects.values('coordinates', 'location')
	
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		
		for place in other_places:
			if place['coordinates'].split(",") != ['']:
				lat = float(place['coordinates'].split(",")[0])
				lng = float(place['coordinates'].split(",")[1])
				current_lat = float(instance.coordinates.split(",")[0])
				current_lng = float(instance.coordinates.split(",")[1])
				
				# Calculate places within a certain distance
				distance = calc_dist(current_lat, current_lng, lat, lng)
		
				if distance < 50.0 and instance.location != place['location']:
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
	singleskill = SingleSkillForm(data=request.POST)
	query = request.GET.get("q")
	if query:
		form.fields['skills'].queryset = form.fields['skills'].queryset.filter(Q(skill__icontains=query))
		
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user =request.user
		instance.save()
		form.
	if singleskill.is_valid():
		instance = singleskill.save(commit=False)
		instance.save()

	context = {
		"form": form,
		'singleskill': singleskill,
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

def current_opportunities(request):
	current = Create_opportunity.objects.filter(
		Q(user__exact=request.user.id)&
		Q(stopping_date__gt=timezone.now())&
		Q(starting_date__lte=timezone.now() + timedelta(days=30))
		)
	context = {
		'current':current,
	}
	return render(request, 'profiles/current_opportunities.html', context)
	
def single_request(request, id=None):
	opportunity = get_object_or_404(Create_opportunity, id = id)
	print opportunity.skills
	context = {
		'opportunity':opportunity,
	}
	return render(request, 'profiles/single_request.html', context)
#############################################################
#frank

#create opportunity form view
def create_opportunity_form(request):
    form = addForm(data = request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.user = request.user
        print form.cleaned_data.get("description")
        instance.save()
		form.save_m2m()
        
        return redirect('/seeker/')
    context = {
        'form' : form
    }
    return render(request, 'profiles/create_opportunity.html', context)
    
def browse(request):	
    show_items = Create_opportunity.objects.order_by('-created_date')
    context = {
        'show_items': show_items
    }
    return render(request, 'profiles/browse.html', context)
    
###############################################################    