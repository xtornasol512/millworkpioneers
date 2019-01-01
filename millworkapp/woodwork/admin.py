from django.contrib import admin

from core.admin import ImageRenderAdmin
from .models import WoodworkPage

class WoodworkPageAdmin(ImageRenderAdmin, admin.ModelAdmin):
    ''' Custom woddwork admin '''
    list_display = [
        'title',
    ]

admin.site.register(WoodworkPage, WoodworkPageAdmin)
