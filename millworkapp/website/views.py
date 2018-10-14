from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic import ListView, DetailView

from gallery.models import Project, Service
from company.models import Client
from .models import (
    AboutPage,
    ContactPage,
    ProjectsPage,
)

def favicon(request):
    ''' Fix favicon '''
    return redirect(settings.STATIC_URL + "brand/icons/favicon-32x32.png", permanent=True)

def about(request):
    ''' About View'''
    client_members = Client.objects.all()
    about_page = AboutPage.objects.first()
    context = {
        'client_members': client_members,
        "about_page": about_page,
    }
    return render(request, 'website/about.html', context)


def contact(request):
    ''' contact View'''
    contact_page = ContactPage.objects.first()
    context = {
        "contact_page": contact_page,
    }
    return render(request, 'website/contact.html')



class ProjectsView(ListView):
    ''' Custom View '''
    model = Project
    template_name = 'website/projects.html'
    context_object_name = 'projects'
    paginate_by = 3
    queryset = Project.objects.display_on_website()

    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data(**kwargs)
        context.update({
            "page_settings": ProjectsPage.objects.first(),
        })
        return context

class ProjectsDetail(DetailView):
    ''' Custom View '''
    template_name = 'website/project_detail.html'
    slug_name = 'slug'
    model = Project
    context_object_name = 'project'


class ServiceGallery(DetailView):
    template_name = 'website/service_gallery.html'
    slug_name = 'slug'
    model = Service
    context_object_name = 'service'

