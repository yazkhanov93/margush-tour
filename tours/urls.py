from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("inside_tours/", views.tourInsideCountry, name="inside_tours"),
    path("inside_tour_detail/<int:pk>/", views.singleTourInsideCountry, name="inside_tour_detail"),
]