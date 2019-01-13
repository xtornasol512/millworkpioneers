from django.db import models

from core.models import WebsiteModelPage
from core.behaviors import Timestampable


class WoodworkPage(Timestampable, WebsiteModelPage, models.Model):
    ''' Page Model '''
    title = models.CharField("Page title",blank=True, max_length=255, default="Wodwork Page")
    main_video = models.URLField("Youtube or vimeo URL", blank=True)

    class Meta:
        verbose_name_plural = "Woodwork Pioneers Page"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def get_video_id(self):
        ''' Get the ID for url link '''
        return self.main_video.split("/")[-1]
