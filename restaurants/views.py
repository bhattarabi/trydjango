import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
	template_name = "home.html"
		
	def get_context_data(self, *args, **kwargs):
		#context = super(HomeView, self).get_context_data(*args, **kwargs)
		l = [random.randint(1,100) for i in range(5)]
		context = {
			"the_list":l, 
			"bool_var": True, 
			"rand_num": random.randint(1, 100)
		}
		return context
		
class AboutView(TemplateView):
	template_name = "about.html"

class ContactView(TemplateView):
	template_name = "contacts.html"

