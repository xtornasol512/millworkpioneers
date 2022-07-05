from django.contrib import admin

from core.admin import ImageRenderAdmin
from .models import (
    HomePage,
    ContactPage,
    AboutPage,
    CareersPage,
    GalleryPage,
    ProjectsPage,
    HomePhoto,
    HomeLogoHeader
)

class PhotoPageInline(ImageRenderAdmin, admin.StackedInline):
    model = HomePhoto
    extra = 1


class LogoHeaderInline(ImageRenderAdmin, admin.StackedInline):
    model = HomeLogoHeader
    extra = 0


class HomePageAdmin(ImageRenderAdmin, admin.ModelAdmin):
    '''Custom Model Admin '''
    inlines = [PhotoPageInline, LogoHeaderInline, ]


class ContactPageAdmin(ImageRenderAdmin, admin.ModelAdmin):
    ''' Custom Client  admin '''
    list_display = [
        'title',
    ]


class AboutPageAdmin(ImageRenderAdmin, admin.ModelAdmin):
    ''' Custom Quote admin '''
    list_display = [
        'title',
    ]


class CareersPageAdmin(ImageRenderAdmin, admin.ModelAdmin):
    ''' Custom Quote admin '''
    list_display = [
        'title',
    ]


class GalleryPageAdmin(ImageRenderAdmin, admin.ModelAdmin):
    ''' Custom Quote admin '''
    list_display = [
        'title',
    ]


class ProjectsPageAdmin(ImageRenderAdmin, admin.ModelAdmin):
    ''' Custom Quote admin '''
    list_display = [
        'title',
    ]


admin.site.register(HomePage, HomePageAdmin)
admin.site.register(ContactPage, ContactPageAdmin)
admin.site.register(AboutPage, AboutPageAdmin)
admin.site.register(CareersPage, CareersPageAdmin)
admin.site.register(GalleryPage, GalleryPageAdmin)
admin.site.register(ProjectsPage, ProjectsPageAdmin)

