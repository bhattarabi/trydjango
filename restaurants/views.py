import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
	l = [random.randint(1,100) for i in range(5)]
	context = {
		"the_list":l, 
		"bool_var": True, 
		"rand_num": random.randint(1, 100)
	}
	return render(request, "home.html", context)   #response

def about(request):
	context = {
	}
	return render(request, "about.html", context)   #response

def contacts(request):
	context = {
	}
	return render(request, "contacts.html", context)   #response
