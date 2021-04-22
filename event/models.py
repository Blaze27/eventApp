from django.db import models
from taggit.managers import TaggableManager
from places.models import Place
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel
# from datetime import datetime, timedelta


TAGGIT_CASE_INSENSITIVE = True

class Event(TimeStampedModel):
    title = models.CharField(max_length=200)
    place = models.ForeignKey(Place, default=None, on_delete=models.CASCADE)
    tags = TaggableManager()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    


class EventTime(models.Model):
    event_date = models.DateField(null=True)
    event_time = models.TimeField(null=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.event_time, self.event_date)


    

