from django.shortcuts import render, reverse, get_object_or_404
from .models import *


def homepage(request):
    tour_inside = TourInCountry.objects.all()[:4]
    tour_outside = TourOutCountry.objects.all()[:4]
    banner = BannerHomePage.objects.all()
    context = {
        "tour_inside": tour_inside,
        "tour_outside":tour_outside,
        "banner": banner,
    }
    return render(request, "index.html", context)


def tourInsideCountry(request):
    tour = TourInCountry.objects.all()
    banner = BannerTourPage.objects.all()
    context = {
        "tours":tour,
        "banner":banner,
    }
    return render(request, "insideTours.html", context)


def insideTourDetail(request, pk):
    tour = TourInCountry.objects.get(id=pk)
    roadmap = TourInCountryRoadMap.objects.all()
    related_tours = TourInCountry.objects.all()
    banner = BannerTourPage.objects.all()
    tour_image = TourInCountryImage.objects.filter(tour=tour)
    visa = VisaInfo.objects.last()
    form = None
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        form = OrderTourInCountry.objects.create(
            tour = tour,
            fullname=fullname,
            email=email,
            phone=phone,
            message=message
        )
    context = {
        "tour": tour,
        "roadmap":roadmap,
        "related_tours":related_tours,
        "banner":banner,
        "tour_image":tour_image,
        "visa":visa,
    }
    return render(request, "insideTourDetail.html", context)


def tourOutsideCountry(request):
    tour = TourOutCountry.objects.all()
    banner = BannerTourPage.objects.all()
    context = {
        "tours":tour,
        "banner":banner,
    }
    return render(request, "outsideTour.html", context)


def country_list(request, id):
    country = get_object_or_404(Country, id=id)
    tour = TourOutCountry.objects.filter(country=country)
    banner = BannerTourPage.objects.all()
    context = {
        "country":country,
        "tours":tour,
        "banner":banner,
    }
    return render(request, "country.html", context)


def outSideTourDetail(request, pk):
    tour = TourOutCountry.objects.get(id=pk)
    roadmap = TourOutCountryRoadMap.objects.all()
    related_tours = TourOutCountry.objects.all()
    banner = BannerTourPage.objects.all()
    visa = VisaInfoAbroad.objects.last()
    form = None
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        form = OrderTourOutCountry.objects.create(
            tour = tour,
            fullname=fullname,
            email=email,
            phone=phone,
            message=message
        )
    context = {
        "tour":tour,
        "roadmap":roadmap,
        "related_tours":related_tours,
        "banner":banner,
        "visa":visa,
    }
    return render(request, "outsideTourDetail.html", context)