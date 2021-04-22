from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .forms import PlaceForm
from django.contrib import messages
# Create your views here.

from places.models import Place

def index(request):
    return render(request, 'index.html')

def sortCity(request):
    distinct_cities = Place.objects.distinct('city')
    return render(request, 'places/sortcity.html', context={'distinct_cities' : distinct_cities})

def all_place_in_city(request, cityname):
    list_of_place = Place.objects.filter(city=cityname)
    return render(request, 'places/sorted_by_city.html', context={'list_of_place' : list_of_place})



def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        
        if form.is_valid():
            x = form.save(commit=False)
            x.save()
            messages.success(request, 'Place added successfully.')
            return redirect('event:create-event')
    else:
        form = PlaceForm()
    
    return render(request, 'places/add_place.html', {"form":form})

class PlacesListView(generic.ListView):
    model = Place


class PlacesDetailView(generic.DetailView):
    model = Place