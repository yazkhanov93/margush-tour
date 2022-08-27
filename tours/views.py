from django.shortcuts import render, reverse, get_object_or_404
from .models import *


contact = Contacts.objects.last()
feedbacks = Feedback.objects.filter(show=True)

def homepage(request):
    tour_inside = TourInCountry.objects.all()[:4]
    tour_outside = TourOutCountry.objects.all()[:4]
    banner = BannerHomePage.objects.all()
    feedback = None
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(
            fullname=fullname,
            email=email,
            message=message
        )
    context = {
        "tour_inside": tour_inside,
        "tour_outside":tour_outside,
        "banner": banner,
        "contacts":contact,
        "feedbacks":feedbacks,
    }
    return render(request, "index.html", context)


def tourInsideCountry(request):
    tour = TourInCountry.objects.all()
    banner = BannerTourPage.objects.all()
    feedback = None
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(
            fullname=fullname,
            email=email,
            message=message
        )
    context = {
        "tours":tour,
        "banner":banner,
         "contacts":contact,
        "feedbacks":feedbacks,
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
        feedback = None
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(
            fullname=fullname,
            email=email,
            message=message
        )
    context = {
        "tour": tour,
        "roadmap":roadmap,
        "related_tours":related_tours,
        "banner":banner,
        "tour_image":tour_image,
        "visa":visa,
         "contacts":contact,
        "feedbacks":feedbacks,
    }
    return render(request, "insideTourDetail.html", context)


def tourOutsideCountry(request):
    tour = TourOutCountry.objects.all()
    banner = BannerTourPage.objects.all()
    feedback = None
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(
            fullname=fullname,
            email=email,
            message=message
        )
    context = {
        "tours":tour,
        "banner":banner,
         "contacts":contact,
        "feedbacks":feedbacks,
    }
    return render(request, "outsideTour.html", context)


def country_list(request, id):
    country = get_object_or_404(Country, id=id)
    tour = TourOutCountry.objects.filter(country=country)
    banner = BannerTourPage.objects.all()
    feedback = None
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(
            fullname=fullname,
            email=email,
            message=message
        )
    context = {
        "country":country,
        "tours":tour,
        "banner":banner,
         "contacts":contact,
        "feedbacks":feedbacks,
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
    feedback = None
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(
            fullname=fullname,
            email=email,
            message=message
        )
    context = {
        "tour":tour,
        "roadmap":roadmap,
        "related_tours":related_tours,
        "banner":banner,
        "visa":visa,
         "contacts":contact,
        "feedbacks":feedbacks,
    }
    return render(request, "outsideTourDetail.html", context)


def aboutCompany(request):
    post = AboutCompany.objects.all()
    banner = BannerAboutUsPage.objects.last()
    image = AboutCompanyImage.objects.all()
    team = Team.objects.all()
    transport = Transport.objects.all()
    transport_image = TransportImage.objects.all()
    feedback = None
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(
            fullname=fullname,
            email=email,
            message=message
        )
    context = {
        "post":post,
        "image":image,
        "team":team,
        "transport":transport,
        "transport_image":transport_image,
        "banner":banner,
        "contacts":contact,
        "feedbacks":feedbacks,
    }
    return render(request, "about_us.html", context)


def aboutCountry(request):
    post = AboutCountry.objects.all()
    banner = BannerAboutUsPage.objects.last()
    geography = Geography.objects.all()
    feedback = None
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(
            fullname=fullname,
            email=email,
            message=message
        )
    context = {
        "post":post,
        "banner":banner,
        "contacts":contact,
        "feedbacks":feedbacks,
        "geography":geography,
    }
    return render(request, "about_country.html", context)


def tourInformation(request):
    info = TourInformation.objects.all()
    banner = BannerAboutUsPage.objects.last()
    feedback = None
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(
            fullname=fullname,
            email=email,
            message=message
        )
    context = {
        "info":info,
        "banner":banner,
        "contacts":contact,
        "feedbacks":feedbacks,
    }
    return render(request, "tour_information.html", context)


def news(request):
    news = News.objects.all()
    banner = BannerNewsPage.objects.last()
    last_news = News.objects.last()
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(
            fullname=fullname,
            email=email,
            message=message
        )
    context = {
        "banner":banner,
        "last":last_news,
        "news":news,
         "contacts":contact,
        "feedbacks":feedbacks,
    }
    return render(request, "news.html", context)


def news_detail(request, pk):
    news_detail = News.objects.get(id=pk)
    banner = BannerNewsPage.objects.last()
    news = News.objects.all()
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(
            fullname=fullname,
            email=email,
            message=message
        )
    context = {
        "news_detail":news_detail,
        "news":news,
        "banner":banner,
        "contacts":contact,
        "feedbacks":feedbacks,
    }
    return render(request, "news_detail.html", context)