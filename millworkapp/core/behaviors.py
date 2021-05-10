# -*- encoding: utf-8 -*-
''' Model behaviors functions that are repit between models '''
from django.db import models


class Timestampable(models.Model):
    ''' Abstract class for Timestampable created_at and updated_at '''

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PlayeableVideo(models.Model):
	""" Share methods for manage video urls """

	main_video = models.URLField("Youtube URL",
					blank=True, default="https://youtu.be/CZb9XTONNkA",
					help_text="Copy from youtube page")

	class Meta:
		abstract = True

	@property
	def get_video_id(self):
		return self.main_video.split("/")[-1]
