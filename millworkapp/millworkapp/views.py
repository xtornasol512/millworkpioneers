from django.shortcuts import render

from gallery.models import Review, Project, Service
from website.models import HomePage

def home(request):
    ''' Home simple view '''
    TOTAL_PROJECTS = 3
    REVIEW_PROJECTS = 6

    reviews = Review.objects.all()[:REVIEW_PROJECTS]
    services = Service.objects.all()
    homepage = HomePage.objects.first()

    context = {
        "reviews" : reviews,
        "services" : services,
        "homepage" : homepage,
    }

    return render(request, "website/home.html", context)
