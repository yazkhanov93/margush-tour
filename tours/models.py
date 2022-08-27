from django.db import models
from django.urls import reverse


class Geography(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="geography_image/")
    description = models.TextField()

    class Meta:
        verbose_name_plural = "География"

    def __str__(self):
        return self.name


class AboutCountry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="about_country_image/")

    class Meta:
        verbose_name_plural = "О стране"

    def __str__(self):
        return self.name


class Transport(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Транспорт"

    def __str__(self):
        return self.name

class TransportImage(models.Model):
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="transport_image/")

    class Meta:
        verbose_name_plural = "Добавить Фото"

    def __str__(self):
        return self.transport.name

class AboutCompany(models.Model):
    name = models.CharField(max_length=255)
    headline = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "О Нас"

    def __str__(self):
        return self.name

class AboutCompanyImage(models.Model):
    post = models.ForeignKey(AboutCompany, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="about_us_image/")

    class Meta:
        verbose_name_plural = "Добавить Фото"
    
    def __str__(self):
        return self.post.name


class Team(models.Model):
    fullname = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    image = models.ImageField(upload_to="team_image/")

    class Meta:
        verbose_name_plural = "Наши Сотрудники"

    def __str__(self):
        return self.fullname


class Contacts(models.Model):
    address = models.CharField(max_length=255)
    location = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    telegram = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    vk = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.address


class Feedback(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    message = models.TextField()
    show = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Отзывы Клиентов"

    def __str__(self):
        return self.fullname



class ExchangeRate(models.Model):
    usd = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Курс доллара"

    def __str__(self):
        return str(self.usd)

class Country(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Страны"

    # def get_absolute_url(self):
    #     return reverse('country_list', args=[self.slug])

    def __str__(self):
        return self.name


class TourInCountry(models.Model):
    name = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to="tour_image/")
    image2 = models.ImageField(upload_to="tour_image/")
    location = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    popular = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Туры внутри страны"

    def tmPrice(self):
        try:
            dollar = ExchangeRate.objects.latest("id")
            price = self.price * dollar.usd
            return price
        except:
            return self.price


class TourInCountryImage(models.Model):
    tour = models.ForeignKey(TourInCountry, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="tour_image/")

    class Meta:
        verbose_name_plural = "Добавить больше фото"

    def __str__(self):
        return self.tour.name


class TourInCountryRoadMap(models.Model):
    tour = models.ForeignKey(TourInCountry, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="tour_image/")

    class Meta:
        verbose_name_plural = "Маршрут"

    def __str__(self):
        return self.name

class OrderTourInCountry(models.Model):
    tour = models.ForeignKey(TourInCountry, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Заявки на внутренные туры"
    
    def __str__(self):
        return self.fullname




# Tour out of the country
class TourOutCountry(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to="tour_image/")
    image2 = models.ImageField(upload_to="tour_image/")
    location = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    popular = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Туры за рубежом"

    def tmPrice(self):
        try:
            usd = ExchangeRate.objects.latest("id")
            price = self.price * usd.usd
            return price
        except:
            return 0


class TourOutCountryImage(models.Model):
    tour = models.ForeignKey(TourOutCountry, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="tour_image/")

    class Meta:
        verbose_name_plural = "Добавить больше фото"

    def __str__(self):
        return self.tour.name


class TourOutCountryRoadMap(models.Model):
    tour = models.ForeignKey(TourOutCountry, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="tour_image/")

    class Meta:
        verbose_name_plural = "Маршрут"

    def __str__(self):
        return self.name


class OrderTourOutCountry(models.Model):
    tour = models.ForeignKey(TourOutCountry, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Заявки на туры за рубежом"
    
    def __str__(self):
        return self.fullname



class BannerHomePage(models.Model):
    name = models.CharField(max_length=255)
    file1 = models.FileField(upload_to="banner_file/")
    file2 = models.FileField(upload_to="banner_file/")
    file3 = models.FileField(upload_to="banner_file/")

    class Meta:
        verbose_name_plural = "Баннер для главного страница"
        ordering = ("-id",)

    def __str__(self):
        return self.name

class BannerTourPage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to="banner_file/")
    
    class Meta:
        verbose_name_plural = "Баннер для тур страницы"
        ordering = ("-id",)

    def __str__(self):
        return self.name

class BannerNewsPage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to="banner_file/")
    

    class Meta:
        verbose_name_plural = "Баннер для страница новастей"
        ordering = ("-id",)

    def __str__(self):
        return self.name


class BannerAboutUsPage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    file1 = models.FileField(upload_to="banner_file/")
   

    class Meta:
        verbose_name_plural = "Баннер для страница О нас"
        ordering = ("-id",)

    def __str__(self):
        return self.name


class VisaInfo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Информация про Виза Туркменистана"

    def __str__(self):
        return self.name

class VisaInfoAbroad(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Информация про за рубежная Виза "

    def __str__(self):
        return self.name


class TourInformation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="tour_information_image/", blank=True, null=True)
    video = models.FileField(upload_to="tour_information_image/", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Информация о путишествии"

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="news_image/")
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Новости"
        ordering = ("-updated",)
    
    def __str__(self):
        return self.name