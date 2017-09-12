from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurantLocation

class RestaurantListView(ListView):
    #template_name = "restaurants/restaurants_list.html"
    def get_queryset(self):
        slug = self.kwargs.get("category")
        if slug:
            queryset = RestaurantLocation.objects.filter(category__iexact=slug)
        else:
            queryset = RestaurantLocation.objects.all()
        
        return queryset
    
    
class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()
    
    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
        return context

