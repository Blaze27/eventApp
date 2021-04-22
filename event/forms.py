from django import forms
from django.contrib.gis import forms
from leaflet.forms.widgets import LeafletWidget
from .models import Event, EventTime


class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = (
            'title',
            'place',
            'tags',
            )
        # widgets = {'place':LeafletWidget()}

class EventTimeForm(forms.ModelForm):
    class Meta:
        model = EventTime
        fields = (
            'event_date',
            'event_time',
        )


