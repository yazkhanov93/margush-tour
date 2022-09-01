from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("inside_tours/", views.tourInsideCountry, name="inside_tours"),
    path("inside_tour_detail/<int:pk>/",
         views.insideTourDetail, name="inside_tour_detail"),
    path("outside_tours/", views.tourOutsideCountry, name="outside_tours"),
    path("country_list/<int:id>/", views.country_list, name="country_list"),
    path("outside_tour_detail/<int:pk>/",
         views.outSideTourDetail, name="outside_tour_detail"),
    path("about_company/", views.aboutCompany, name="about_company"),
    path("about_country/", views.aboutCountry, name="about_country"),
    path("tour_information/", views.tourInformation, name="tour_information"),
    path("news/", views.news, name="news"),
    path("news_detail/<int:pk>/", views.news_detail, name="news_detail"),
]
