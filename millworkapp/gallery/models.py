from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.safestring import mark_safe

from core.behaviors import Timestampable

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

    def __str__(self):
        ''' Get name '''
        return self.name


