from django.db import models

from .querysets import ProjectQueryset

class ProjectManager(models.Manager):
    ''' Custom actions with Projects '''

    def get_queryset(self):
        return ProjectQueryset(self.model, using=self._db)

    def all_completed(self):
        return self.get_queryset().all_completed()

    def all_in_progress(self):
        return self.get_queryset().all_in_progress()
