from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.safestring import mark_safe

from core.behaviors import Timestampable
from .managers import ProjectManager

class Review(Timestampable, models.Model):
    ''' Review Model '''
    name = models.CharField("Reviewer name", max_length=255, default="")
    description = models.TextField(blank=True, default="")
    place = models.CharField("Place name", blank=True, max_length=255, default="", help_text='Square Image MIN_SIZE=320x320, MAX_SIZE=900x900')

    avatar = models.ImageField(upload_to='avatars')
    # avatar_thumbnail = ImageSpecField(source='avatar',
    #                                   processors=[ResizeToFill(100, 50)],
    #                                   format='JPEG',
    #                                   options={'quality': 60})

    class Meta:
        ''' Custom Model metadata '''
        verbose_name_plural = "Reviews(★★★★★)"
        ordering = ['-created_at']

    def __str__(self):
        ''' Get name '''
        return self.name


class Tag(Timestampable, models.Model):
    ''' Tag table '''
    name = models.CharField("Tag name", max_length=255, default="", help_text="Prefer use without spaces (Could be with  '_' or '-')")
    description = models.CharField("Short description", blank=True, max_length=255, default="")

    class Meta:
        ''' Custom Model metadata '''
        verbose_name_plural = "Photo Tags"
        ordering = ['-created_at']

    def __str__(self):
        ''' Return string data '''
        return self.name


class Photo(Timestampable, models.Model):
    ''' Gallery Photos Page '''
    title = models.CharField("Photo title", max_length=255, default="")
    description = models.TextField("Short description", blank=True, default="")
    picture = models.ImageField(upload_to='gallery_photos')
    tags = models.ManyToManyField("gallery.Tag", related_name="photos", blank=True)
    project = models.ForeignKey("gallery.Project", models.SET_NULL, blank=True, null=True, related_name="photos", help_text='Select one project')
    service = models.ForeignKey("gallery.Service", models.SET_NULL, blank=True, null=True, related_name="photos", help_text='Select one Service')

    class Meta:
        ''' Custom Model metadata '''
        verbose_name_plural = "Gallery Photos"
        ordering = ['-created_at']

    def __str__(self):
        ''' Return string data '''
        return self.title


class Project(Timestampable, models.Model):
    ''' Project Model '''
    title = models.CharField("Title of project", max_length=255, default="")
    slug = models.SlugField("Url slug", max_length=255, blank=True, default="", help_text='This field is auto-generated')

    description = models.TextField(blank=True, default="")
    client = models.CharField("Client name", max_length=255, blank=True, default="")
    STATUS_PROJECT_OPTIONS = (
        ("COMPLETED", 'Completed'),
        ("IN PROGRESS", 'In progress'),
    )
    status_project = models.CharField("Status of the project", blank=True, max_length=255, choices=STATUS_PROJECT_OPTIONS, default="COMPLETED", help_text='Select one')
    main_picture = models.ImageField("Main picture for project", upload_to='projects', blank=True)
    is_display_on_website = models.BooleanField("Will display on site?", default=True, help_text='Select "Yes" to display on site')

    objects = ProjectManager()

    class Meta:
        ''' Custom Model metadata '''
        verbose_name_plural = "Millwork Projects"
        ordering = ['-created_at']

    def __str__(self):
        ''' Return string data '''
        return self.title



class Service(Timestampable, models.Model):
    ''' Service '''
    name = models.CharField("Name", max_length=255, default="")
    slug = models.SlugField("Url slug", max_length=255, blank=True, default="", help_text='This field is auto-generated')
    description = models.TextField(blank=True, default="")
    is_display_on_website = models.BooleanField("Will display on site?", default=True, help_text='Select "Yes" to display on site')

    main_picture =  models.ImageField("Main picture for project", upload_to='services', blank=True)

    class Meta:
        ''' Custom Model metadata '''
        verbose_name_plural = "Millwork Services"
        ordering = ['-created_at']

    def __str__(self):
        ''' Return string data '''
        return self.name
