from django.shortcuts import render

from gallery.models import Review

def home(request):
    ''' Home simple view '''
    reviews = Review.objects.all()

    context = {
        "reviews": reviews
    }

    return render(request, "website/home.html", context)
