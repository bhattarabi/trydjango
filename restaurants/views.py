from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import RestaurantLocation


from .forms import RestaurantCreateForm, RestaurantLocationCreateForm


def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/restaurants/")
    
    template_name = "restaurants/form.html"
    context = {"form":form}
    return render(request, template_name, context)



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


class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = "restaurants/form.html"
    success_url = "/restaurants/"

   
