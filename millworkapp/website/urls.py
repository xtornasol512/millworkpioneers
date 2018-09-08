from django.conf.urls import include, url


from .views import about, contact, favicon
from company.views import ContactFormView, AskQuoteFormView


urlpatterns = [
    url(r'^favicon.ico$', favicon, name="favicon"),
    url(r'^contact$', contact, name='contact'),
    url(r'^forms/contact/', ContactFormView.as_view(), name='contact_form'),
    url(r'^forms/askquote/', AskQuoteFormView.as_view(), name='askquote_form'),
    url(r'^about$', about, name='about'),
]
