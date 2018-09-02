from django.conf.urls import include, url

from .views import about, contact


urlpatterns = [
    url(r'^contact$', contact, name='contact'),
    url(r'^about$', about, name='about'),
]
