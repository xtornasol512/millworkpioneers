from django.db import models

from core.models import WebsiteModelPage
from core.behaviors import Timestampable, PlayeableVideo


class HomePage(Timestampable, models.Model):
    ''' Page Model '''
    title = models.CharField(
        "Page title", blank=True, max_length=255, default="Home Page")

    class Meta:
        verbose_name_plural = "Home Page"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ContactPage(Timestampable, WebsiteModelPage, models.Model):
    ''' Page Model '''
    title = models.CharField(
        "Page title", blank=True, max_length=255, default="Contact Page")
    map_latitude = models.CharField(
        "Latitude Coordinates", max_length=50, blank=True, default="33.8080843",
        help_text='Use google url coordinates')
    map_longitude = models.CharField(
        "Longitude Coordinates", max_length=50, blank=True, default="-118.0604532",
        help_text='Use google url coordinates')
    map_address = models.CharField(
        "Map Address", max_length=255, blank=True,
        default="MillworkPioneers Address")

    class Meta:
        verbose_name_plural = "Contact Page"


class AboutPage(PlayeableVideo, Timestampable, WebsiteModelPage, models.Model):
    ''' Page Model '''
    title = models.CharField("Page title", blank=True, max_length=255, default="About Page")

    class Meta:
        verbose_name_plural = "About Page"


class CareersPage(Timestampable, WebsiteModelPage, models.Model):
    ''' Page Model '''
    title = models.CharField("Page title", blank=True, max_length=255, default="Careers Page")

    class Meta:
        verbose_name_plural = "Careers Page"


class GalleryPage(Timestampable, WebsiteModelPage, models.Model):
    ''' Page Model '''
    title = models.CharField("Page title", blank=True, max_length=255, default="Gallery Page")

    class Meta:
        verbose_name_plural = "Gallery Page"


class ProjectsPage(Timestampable, WebsiteModelPage, models.Model):
    ''' Page Model '''
    title = models.CharField("Page title", blank=True, max_length=255, default="Projects Page")

    class Meta:
        verbose_name_plural = "Projects Page"


class HomePhoto(Timestampable, models.Model):
    ''' Gallery Photos Page '''
    title = models.CharField("Photo title", max_length=255, default="")
    description = models.TextField("Short description", blank=True, default="")
    picture = models.ImageField(upload_to='home_photos')
    page = models.ForeignKey(
        "website.HomePage", models.SET_NULL, blank=True, null=True,
        related_name='page_photos', help_text='Select Home Page')

    class Meta:
        verbose_name_plural = "Home Website Photos"
        ordering = ['-created_at']

    def __str__(self):
        ''' Return string data '''
        return self.title


class HomeLogoHeader(Timestampable, models.Model):
    ''' Gallery Header Page on Landing '''
    title = models.CharField("Photo title", max_length=255, default="")
    description = models.TextField(
        "Short description", default="",
        help_text="This help on SEO, use a brief description of logo")
    picture = models.ImageField(
        upload_to='home_photos_header',
        help_text="Must have to be edited before, 900x506 pixeles! For better quality")
    page = models.ForeignKey(
        "website.HomePage", models.SET_NULL, blank=True, null=True,
        related_name='page_header_photos', help_text='Select Home Page')
    is_display_on_website = models.BooleanField(
        "Will display on site?", default=True,
        help_text='Select "Yes" to display on site')
    site_url = models.URLField("Site url", blank=True, default="#")

    class Meta:
        verbose_name_plural = "Home Website Header Logos"
        ordering = ['-created_at']

    def __str__(self):
        ''' Return string data '''
        return self.title
