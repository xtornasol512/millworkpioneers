from django.shortcuts import render

from gallery.models import Review, Project, Service

def home(request):
    ''' Home simple view '''
    LATEST_PROJECTS = 2
    TOTAL_PROJECTS = 3
    REVIEW_PROJECTS = 6

    reviews = Review.objects.all()[:REVIEW_PROJECTS]
    projects = Project.objects.all_completed()[:TOTAL_PROJECTS]
    latest_projects = Project.objects.all()[:LATEST_PROJECTS]
    in_progress = Project.objects.all_in_progress()[:TOTAL_PROJECTS]
    services = Service.objects.all()

    context = {
        "reviews": reviews,
        "projects": projects,
        "in_progress": in_progress,
        "services": services,
        "latest_projects": latest_projects,
    }

    return render(request, "website/home.html", context)
