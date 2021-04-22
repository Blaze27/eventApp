import django_filters
from .models import EventTime, Event
from django_filters import DateRangeFilter,DateFilter

class EventFilters(django_filters.FilterSet):

    event_year = django_filters.NumberFilter(field_name='event_date', lookup_expr='year', label='Event Year')
    # event_year__gt = django_filters.NumberFilter(field_name='event_date', lookup_expr='year__gt')
    # event_year__lt = django_filters.NumberFilter(field_name='event_date', lookup_expr='year__lt')
    event_month = django_filters.NumberFilter(field_name='event_date', lookup_expr='month', label="Event Mnth")
    event_day = django_filters.NumberFilter(field_name='event_date', lookup_expr='day', label="Event Day")
    # event_between_dates = django_filters.DateFromToRangeFilter(field_name='event_date', label='Events between dates')

    class Meta:
        model = EventTime
        fields = ['event_date', 'event_time']