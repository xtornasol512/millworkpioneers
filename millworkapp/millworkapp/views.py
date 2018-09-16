from django.shortcuts import render

from gallery.models import Review, Project, Service

def home(request):
    ''' Home simple view '''
    reviews = Review.objects.all()
    projects = Project.objects.all_completed()
    in_progress = Project.objects.all_in_progress()
    services = Service.objects.all()

    context = {
        "reviews": reviews,
        "projects": projects,
        "in_progress": in_progress,
        "services": services,
    }

    return render(request, "website/home.html", context)
