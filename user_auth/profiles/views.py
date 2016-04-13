from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from urllib import quote_plus
from django.contrib import messages

from .models import Opportunity


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