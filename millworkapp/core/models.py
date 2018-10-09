from django.db import models

class WebsiteModelPage(models.Model):
    ''' Website header Photo '''

    picture = models.ImageField(upload_to='website_header')

    class Meta:
        abstract = True

    def __str__(self):
        ''' Return string repr '''
        return self.title
