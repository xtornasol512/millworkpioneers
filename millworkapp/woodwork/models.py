from django.db import models

from core.models import WebsiteModelPage
from core.behaviors import Timestampable, PlayeableVideo


class WoodworkPage(PlayeableVideo, Timestampable, WebsiteModelPage, models.Model):
    ''' Page Model '''
    title = models.CharField("Page title",blank=True, max_length=255, default="Wodwork Page")

    class Meta:
        verbose_name_plural = "Woodwork Pioneers Page"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
