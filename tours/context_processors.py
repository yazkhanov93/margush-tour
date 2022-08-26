from .models import Country

def countries(request):
    return {
        "countries":Country.objects.all()
    }