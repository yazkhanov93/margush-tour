from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("inside_tours/", views.tourInsideCountry, name="inside_tours"),
    path("inside_tour_detail/<int:pk>/", views.insideTourDetail, name="inside_tour_detail"),
    path("outside_tours/", views.tourOutsideCountry, name="outside_tours"),
    path("country_list/<int:id>/", views.country_list, name="country_list"),
    path("outside_tour_detail/<int:pk>/", views.outSideTourDetail, name="outside_tour_detail"),
]