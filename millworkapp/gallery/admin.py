from django.contrib import admin
from django.db import models

from .models import Review
from core.admin import AdminImageWidget


class ReviewAdmin(admin.ModelAdmin):
    ''' Custom Admin model '''

    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }

    list_display = [
        'id',
        'name',
        'description',
    ]
    readonly_fields = ['id', ]



admin.site.register(Review, ReviewAdmin)


