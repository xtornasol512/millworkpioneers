from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic import ListView, DetailView

from gallery.models import Project
from company.models import Client


def favicon(request):
    ''' Fix favicon '''
    return redirect(settings.STATIC_URL + "brand/icons/favicon-32x32.png", permanent=True)

def about(request):
    ''' About View'''
    client_members = Client.objects.all()
    context = {
        'client_members': client_members,
    }
    return render(request, 'website/about.html', context)


def contact(request):
    ''' contact View'''
    return render(request, 'website/contact.html')



class ProjectsView(ListView):
    ''' Custom View '''
    model = Project
    template_name = 'website/projects.html'
    context_object_name = 'projects'
    paginate_by = 3
    queryset = Project.objects.display_on_website()


class ProjectsDetail(DetailView):
    ''' Custom View '''
    template_name = 'website/project_detail.html'
    slug_name = 'slug'
    model = Project
    context_object_name = 'project'

