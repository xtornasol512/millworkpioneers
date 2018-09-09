from django.contrib import admin
from django.db import models

from core.admin import AdminImageWidget
from .models import Review, Tag, Photo


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


class TagAdmin(admin.ModelAdmin):
    ''' Custom Admin model '''
    list_display = [
        'name',
        'description',
    ]

class PhotoAdmin(admin.ModelAdmin):
    ''' Custom Admin model '''
    pass

admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Photo, PhotoAdmin)
