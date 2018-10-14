from django.conf.urls import include, url


from .views import about, contact, favicon
from company.views import ContactFormView, AskQuoteFormView, AskMailFormView, CareersView
from gallery.views import gallery_page
from website.views import ProjectsView, ProjectsDetail, ServiceGallery


urlpatterns = [
    url(r'^favicon.ico$', favicon, name="favicon"),
    url(r'^contact$', contact, name='contact'),
    url(r'^forms/contact/', ContactFormView.as_view(), name='contact_form'),
    url(r'^forms/askquote/', AskQuoteFormView.as_view(), name='askquote_form'),
    url(r'^forms/askmail/', AskMailFormView.as_view(), name='askmail_form'),
    url(r'^about$', about, name='about'),
    url(r'^gallery$', gallery_page, name='gallery'),
    url(r'^projects$', ProjectsView.as_view(), name='projects'),
    url(r'^careers/', CareersView.as_view(), name='careers'),
    url(r'^projects/(?P<slug>[\w-]+)$', ProjectsDetail.as_view(), name='project_detail'),
    # ServiceGallery
    url(r'^services/(?P<slug>[\w-]+)$', ServiceGallery.as_view(), name='service_gallery'),
]
