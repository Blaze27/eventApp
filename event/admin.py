from django.contrib import admin
from .models import Event, EventTime

class TimingInline(admin.StackedInline):
    model = EventTime
    extra = 1

class EventAdmin(admin.ModelAdmin):
    inlines = [TimingInline]

admin.site.register(Event, EventAdmin)
