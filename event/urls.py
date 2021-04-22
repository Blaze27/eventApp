from django.urls import path
from . import views

app_name='event'

urlpatterns = [
    path('', views.index, name = "index"),
    path('all-events/', views.all_events, name = "all-events"),
    path('create-event/', views.create_event, name = "create-event"),
    path('sort-event/', views.TimingListView.as_view(), name = "sort-event"),
    path('event-detail/<int:pk>', views.EventDetail.as_view(), name="event-detail"),
    path('edit-event/<int:pk>', views.edit_event, name = "edit-event"),
]
