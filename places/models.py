from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100)
    location = PointField(default=None)
    description = models.TextField(max_length=3000)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    type_of_place = models.CharField(max_length=100)

    def get_absolute_url(self):
        # pass
        return reverse('place-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
