from django.contrib import admin

from core.admin import ImageRenderAdmin
from .models import Review, Tag, Photo, Project, Service

class PhotoInline(ImageRenderAdmin, admin.StackedInline):
    model = Photo
    extra = 1


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


class ProjectAdmin(ImageRenderAdmin, admin.ModelAdmin):
    ''' Custom Admin Model '''
    inlines = [PhotoInline, ]
    list_filter = ['status_project', 'is_display_on_website', ]
    list_display_links = list_display = [
        'title',
        'status_project',
        'is_display_on_website',
        'created_at',
        'updated_at',
    ]
    fields = [
        'title',
        'slug',
        'status_project',
        'description',
        'client',
        'main_picture',
        'is_display_on_website',
    ]
    prepopulated_fields = {"slug": ("title",)}

class ServiceAdmin(ImageRenderAdmin, admin.ModelAdmin):
    ''' Custom admin model '''
    list_display_links = list_display = [
        'name',
        'description',
        'created_at',
        'updated_at',
    ]


admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
