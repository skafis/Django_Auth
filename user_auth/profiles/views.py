from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	context = {}
	template = 'profiles/index.html'
	return render(request, template, context)
