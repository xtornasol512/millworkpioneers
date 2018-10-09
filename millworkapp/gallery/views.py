from django.shortcuts import render

from .models import Tag, Photo
from website.models import GalleryPage

def gallery_page(request):
    ''' Simple Gallery view '''
    gallery_page = GalleryPage.objects.first()
    context = {
        'tags': Tag.objects.all(),
        'gallery_photos': Photo.objects.all(),
        'gallery_page': gallery_page,

    }
    return render(request, 'website/gallery.html', context)
