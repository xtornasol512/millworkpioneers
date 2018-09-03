from django.conf.urls import include, url


from .views import about, contact, favicon


urlpatterns = [
    url(r'^favicon.ico$', favicon, name="favicon"),
    url(r'^contact$', contact, name='contact'),
    url(r'^about$', about, name='about'),
]
