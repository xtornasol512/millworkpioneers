from django.db import models

from core.models import WebsiteModelPage
from core.behaviors import Timestampable


class HomePage(Timestampable, models.Model):
    ''' Page Model '''
    title = models.CharField("Page title",blank=True, max_length=255, default="Home Page")

    class Meta:
        verbose_name_plural = "Home Page"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ContactPage(Timestampable, WebsiteModelPage, models.Model):
    ''' Page Model '''
    title = models.CharField("Page title",blank=True, max_length=255, default="Contact Page")

    class Meta:
        verbose_name_plural = "Contact Page"


class AboutPage(Timestampable, WebsiteModelPage, models.Model):
    ''' Page Model '''
    title = models.CharField("Page title",blank=True, max_length=255, default="About Page")

    class Meta:
        verbose_name_plural = "About Page"


class CareersPage(Timestampable, WebsiteModelPage, models.Model):
    ''' Page Model '''
    title = models.CharField("Page title",blank=True, max_length=255, default="Careers Page")

    class Meta:
        verbose_name_plural = "Careers Page"


class GalleryPage(Timestampable, WebsiteModelPage, models.Model):
    ''' Page Model '''
    title = models.CharField("Page title",blank=True, max_length=255, default="Gallery Page")

    class Meta:
        verbose_name_plural = "Gallery Page"


class ProjectsPage(Timestampable, WebsiteModelPage, models.Model):
    ''' Page Model '''
    title = models.CharField("Page title",blank=True, max_length=255, default="Projects Page")

    class Meta:
        verbose_name_plural = "Projects Page"


class HomePhoto(Timestampable, models.Model):
    ''' Gallery Photos Page '''
    title = models.CharField("Photo title", max_length=255, default="")
    description = models.TextField("Short description", blank=True, default="")
    picture = models.ImageField(upload_to='home_photos')
    page = models.ForeignKey("website.HomePage", models.SET_NULL, blank=True, null=True, related_name='page_photos', help_text='Select Home Page' )


    class Meta:
        verbose_name_plural = "Home Website Photos"
        ordering = ['-created_at']

    def __str__(self):
        ''' Return string data '''
        return self.title

