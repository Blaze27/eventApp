from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('all_places', views.PlacesListView.as_view(), name="all_places"),
    path('sort_by_city', views.sortCity, name="sort_by_city"),
    path('all_places/<int:pk>', views.PlacesDetailView.as_view(), name = "place-detail"),
]

#  Update url for adding new place

urlpatterns += [
    path('add_place', views.add_place, name="add_place"),
]

# Update url for adding distinct cities

urlpatterns += [
    path('distinct_cities/<str:cityname>', views.all_place_in_city, name="instance-city-place"),
]