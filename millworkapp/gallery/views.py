from django.shortcuts import render

# Create your views here.

def gallery_page(request):
    ''' Simple Gallery view '''
    return render(request, 'website/gallery.html')
