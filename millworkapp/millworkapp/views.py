from django.shortcuts import render

from gallery.models import Review, Project

def home(request):
    ''' Home simple view '''
    reviews = Review.objects.all()
    projects = Project.objects.all_completed()
    in_progress = Project.objects.all_in_progress()

    context = {
        "reviews": reviews,
        "projects": projects,
        "in_progress": in_progress,
    }

    return render(request, "website/home.html", context)
