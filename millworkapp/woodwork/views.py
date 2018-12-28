from django.shortcuts import render
from django.views.generic import View

class WoodworkView(View):
    template_name = 'website/woodwork.html'

    def get(self, request):
        return render(request, self.template_name)
