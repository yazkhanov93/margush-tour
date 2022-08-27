from django.contrib import admin
from .models import *
from . import models


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(TourInformation)
class TourInformationAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(Geography)
class GeographyAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(AboutCountry)
class AboutcountryAdmin(admin.ModelAdmin):
    list_display = ["name",]


class TransportImageInline(admin.StackedInline):
    model = models.TransportImage
    extra = 1

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ["name",]
    inlines = [TransportImageInline]

    save_as = True
    save_on_top = True

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["fullname", "profession"]


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ["address","phone","email"]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["fullname","email", "show"]


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ["usd",]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name",]
    prepopulated_fields = {"slug":("name",)}


class AboutCompanyImageInline(admin.StackedInline):
    model = models.AboutCompanyImage
    extra = 1


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "headline"]
    inlines = [AboutCompanyImageInline]

    save_as = True
    save_on_top = True

""" Tours Inside Country """

class TourInCountryImageInline(admin.StackedInline):
    model = models.TourInCountryImage
    extra = 1


class TourInCountryRoadMapInline(admin.StackedInline):
    model = models.TourInCountryRoadMap
    extra = 1


@admin.register(TourInCountry)
class TourInCountryAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "popular"]
    inlines = [TourInCountryImageInline, TourInCountryRoadMapInline]

    save_as = True
    save_on_top = True

""" Tours abroad """


class TourOutCountryImageInline(admin.StackedInline):
    model = models.TourOutCountryImage
    extra = 1


class TourOutCountryRoadMapInline(admin.StackedInline):
    model = models.TourOutCountryRoadMap
    extra = 1


@admin.register(TourOutCountry)
class TourOutCountryAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "popular"]
    inlines = [TourOutCountryImageInline, TourOutCountryRoadMapInline]

    save_as = True
    save_on_top = True


""" Banner """


@admin.register(BannerHomePage)
class BannerHomePageAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(BannerTourPage)
class BannerTourPageAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(BannerNewsPage)
class BannerNewsPageAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(BannerAboutUsPage)
class BannerAboutUsPageAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(VisaInfo)
class VisaInfoAdmin(admin.ModelAdmin):
    list_display = ["name",]

@admin.register(VisaInfoAbroad)
class VisaInfoAbroadAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(OrderTourInCountry)
class OrderTourInCountryAdmin(admin.ModelAdmin):
    list_display = ["fullname","email","phone"]


@admin.register(OrderTourOutCountry)
class OrderTourOutCountryAdmin(admin.ModelAdmin):
    list_display = ["fullname", "email", "phone"]