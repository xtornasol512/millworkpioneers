from django.shortcuts import render

from gallery.models import Review, Service
from website.models import HomePage
from company.forms import QuoteForm


def home(request):
    ''' Home simple view '''
    REVIEW_PROJECTS = 6

    reviews = Review.objects.all()[:REVIEW_PROJECTS]
    services = Service.objects.all()
    homepage = HomePage.objects.first()
    if homepage is not None:
        header_logos = homepage.page_header_photos.filter(is_display_on_website=True)
    else:
        header_logos = None

    context = {
        "reviews": reviews,
        "services": services,
        "homepage": homepage,
        "form": QuoteForm(),
        "header_logos": header_logos,
    }

    return render(request, "website/home.html", context)
