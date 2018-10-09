from django.shortcuts import render

from gallery.models import Review, Project, Service
from website.models import HomePage

def home(request):
    ''' Home simple view '''
    TOTAL_PROJECTS = 3
    REVIEW_PROJECTS = 6

    reviews = Review.objects.all()[:REVIEW_PROJECTS]
    projects = Project.objects.all_completed()[:TOTAL_PROJECTS]
    in_progress = Project.objects.all_in_progress()[:TOTAL_PROJECTS]
    services = Service.objects.all()
    homepage = HomePage.objects.first()

    context = {
        "reviews" : reviews,
        "projects" : projects,
        "in_progress" : in_progress,
        "services" : services,
        "homepage" : homepage,
    }

    return render(request, "website/home.html", context)
