from django.contrib.gis import forms
from .models import Place



class PlaceForm( forms.ModelForm):
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