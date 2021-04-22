from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Event, EventTime
from .forms import EventForm, EventTimeForm
from django.forms import formset_factory
from places.models import Place
from django.views.generic import DetailView, ListView
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Event
from .filters import EventFilters
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_events(request):
    event_list = Event.objects.all()

    context = {
        'event_list' : event_list,
    }
    return render(request, 'event/all_events.html', context=context)

@login_required
def create_event(request):
    event_form = EventForm(request.POST or None)

    EventTimeFormSet = formset_factory(EventTimeForm, extra=1)
    event_time_form = EventTimeFormSet(request.POST or None)
    
    if event_form.is_valid() and event_time_form.is_valid():
        event_obj = event_form.save()
        event_obj.created_by = request.user
        event_obj.save()
        
        for event_time in event_time_form:
            event_time = event_time.save(commit = False)
            event_time.event = event_obj
            event_time.save()
            messages.success(request, 'Event created successfully.')
        return redirect('event:index')
    
    context = {
        'event_form' : event_form,
        'event_time_form' : event_time_form,
    }



    return render(request, 'event/add_event.html', context=context)

class TimingListView(ListView):
    model = EventTime
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EventFilters(self.request.GET, queryset=self.get_queryset())
        return context

class EventDetail(DetailView):
    model = Event

@login_required
def edit_event(request, pk):
    event_obj = get_object_or_404(Event, id=pk)
    event_time_obj = get_object_or_404(EventTime, id=event_obj.id)

    if event_obj.created_by != request.user:
        messages.warning(request, 'You Cannot edit this event as you are not the one who created it.')
        return redirect('event:event-detail', pk)

    event_form = EventForm(request.POST or None, instance=event_obj)
    event_time_form = EventTimeForm(request.POST or None, instance=event_time_obj)

    if event_form.is_valid() and event_time_form.is_valid():
        event_instance = event_form.save()
        event_instance.created_by = request.user
        event_instance.save()
        event_time_form.save()
        messages.success(request, 'Event edited successfully.')
        return redirect('event:index')
    
    context = {
        # 'event_obj' : event_obj,
        'event_form' : event_form,
        # 'event_time_obj' : event_time_obj,
        'event_time_form' : event_time_form,
    }
    return render(request, 'event/add_event.html', context)

    
    