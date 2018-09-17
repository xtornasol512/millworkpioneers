from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic import View, ListView

from gallery.models import Project


def favicon(request):
    ''' Fix favicon '''
    return redirect(settings.STATIC_URL + "brand/icons/favicon-32x32.png", permanent=True)

def about(request):
    ''' About View'''
    return render(request, 'website/about.html')


def contact(request):
    ''' contact View'''
    return render(request, 'website/contact.html')



class ProjectsView(ListView):
    ''' Custom View '''
    model = Project
    template_name = 'website/projects.html'
    context_object_name = 'projects'
    paginate_by = 10
    queryset = Project.objects.display_on_website()


class ProjectsDetail(View):
    ''' Custom View '''
    template = 'website/project_detail.html'
    context = {}

    def get(self, request, slug):
        ''' Custom get with slug '''
        return render(request, self.template, self.context)

