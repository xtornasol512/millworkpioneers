from django.shortcuts import render

from .models import Tag, Photo

def gallery_page(request):
    ''' Simple Gallery view '''
    context = {
        'tags': Tag.objects.all(),
        'gallery_photos': Photo.objects.all()
    }
    return render(request, 'website/gallery.html', context)
