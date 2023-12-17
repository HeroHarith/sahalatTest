from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="home"),
    path("trips/", views.trips, name="trips"),
    path("trips/<int:pk>/", views.trip, name="trip"),
    path("order/<int:pk>/", views.order, name="order"),
    path("new_trip/", views.new_trip, name="new"),
]