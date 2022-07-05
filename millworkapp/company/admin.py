from django.contrib import admin

from core.admin import ImageRenderAdmin
from .models import Company, Client, Quote


class CompanyAdmin(admin.ModelAdmin):
    pass


class ClientAdmin(ImageRenderAdmin, admin.ModelAdmin):
    ''' Custom Client  admin '''
    list_display_links = list_display = [
        "name",
        "website",
        "headline",
    ]


class QuoteAdmin(admin.ModelAdmin):
    ''' Custom Quote admin '''
    list_display_links = list_display = [
        'id',
        'name',
        'phone',
        'email',
        'company',
        'project',
        'start_date',
        'created_at',
    ]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Quote, QuoteAdmin)
