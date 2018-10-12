''' List of querysets '''
from django.db import models

class ProjectQueryset(models.QuerySet):
    ''' Add custom querysets'''

    def display_on_website(self):
        return self.filter(is_display_on_website=True)

    def all_completed(self):
        return self.display_on_website()

    def all_in_progress(self):
        return self.display_on_website()
