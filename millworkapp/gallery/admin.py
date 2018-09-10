from django.contrib import admin

from core.admin import ImageRenderAdmin
from .models import Review, Tag, Photo


class ReviewAdmin(ImageRenderAdmin, admin.ModelAdmin):
    ''' Custom Admin model '''
    list_display_links = list_display = [
        'id',
        'name',
        'description',
    ]
    readonly_fields = ['id', ]


class TagAdmin(admin.ModelAdmin):
    ''' Custom Admin model '''
    list_display_links = list_display = [
        'id',
        'name',
        'description',
    ]
    readonly_fields = ['id', ]


class PhotoAdmin(ImageRenderAdmin, admin.ModelAdmin):
    ''' Custom Admin model '''
    list_display = list_display_links = [
        'id',
        'title',
        'description',
    ]
    readonly_fields = ['id', ]


admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Photo, PhotoAdmin)
