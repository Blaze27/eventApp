from django.contrib.gis import forms
from .models import Place
from leaflet.forms.widgets import LeafletWidget
from django import forms

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = (
            'name', 
            'location',
            'description', 
            'address', 
            'city',
            'type_of_place',
            
            )
        widgets = {'location' : LeafletWidget()}