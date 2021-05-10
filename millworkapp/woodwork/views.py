from django.shortcuts import redirect
from django.views.generic import ListView

from .models import WoodworkPage
from gallery.models import Project


class WoodworkView(ListView):
    ''' Custom View '''
    model = Project
    template_name = 'website/woodwork.html'
    context_object_name = 'projects'
    paginate_by = 6
    queryset = Project.objects.display_on_website().is_woodwork()

    def get_context_data(self, **kwargs):
        context = super(WoodworkView, self).get_context_data(**kwargs)
        context.update({
            "page_settings": WoodworkPage.objects.first(),
        })
        return context


def woodwork_redirect(response):
    ''' A redirect to woodwork site'''
    return redirect('woodwork')
