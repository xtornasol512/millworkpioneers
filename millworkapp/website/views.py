from django.shortcuts import render

# Create your views here.

def about(request):
    ''' About View'''
    return render(request, 'website/about.html')


def contact(request):
    ''' contact View'''
    return render(request, 'website/contact.html')
