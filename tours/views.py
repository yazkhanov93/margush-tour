from django.shortcuts import render
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


def singleTourInsideCountry(request, pk):
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
    return render(request, "insideSingleTour.html", context)