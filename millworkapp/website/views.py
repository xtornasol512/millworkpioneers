from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.

def favicon(request):
    ''' Fix favicon '''
    return redirect(settings.STATIC_URL + "brand/icons/favicon-32x32.png", permanent=True)

def about(request):
    ''' About View'''
    return render(request, 'website/about.html')


def contact(request):
    ''' contact View'''
    return render(request, 'website/contact.html')
