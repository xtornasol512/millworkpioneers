from django.db import models
from django.contrib.postgres.fields import JSONField
from core.behaviors import Timestampable


class Company(Timestampable, models.Model):
    ''' Company model '''

    title = models.CharField("Title", max_length=255, default="")
    phone = models.CharField("Phone", max_length=50, blank=True, default="")
    fax = models.CharField("Fax", max_length=255, blank=True, default="")
    email = models.EmailField("Email", max_length=255, blank=True)
    headline = models.CharField("Headline", max_length=255, blank=True, default="")
    address = models.CharField("Address", max_length=255, blank=True, default="")
    facebook = models.CharField("Facebook", max_length=255, blank=True, default="")
    twitter = models.CharField("Twitter", max_length=255, blank=True, default="")
    linkedin = models.CharField("Linkedin", max_length=255, blank=True, default="")
    service_area = models.TextField("Service area", blank=True, default="")
    hours_operation = models.TextField("Hours of operation", blank=True, default="")

    data = JSONField(blank=True, default={}, help_text="Metadata")

    class Meta:
        ''' Custom Admin metadata'''
        verbose_name_plural = "Company Settings"
        ordering = ['created_at']

    def __str__(self):
        ''' Display name to object '''
        return self.title


class Client(Timestampable, models.Model):
    ''' Client Model '''
    name = models.CharField("Client name", max_length=255, default="")
    website = models.URLField("Website url", blank=True, max_length=255)
    headline = models.CharField("Company headline", max_length=255, blank=True, default="")

    data = JSONField(blank=True, default={}, help_text="Metadata")

    def __str__(self):
        ''' Display name to object '''
        return self.name
