from django.shortcuts import render

def home(request):
    ''' Home simple view '''
    return render(request, "index.html")
