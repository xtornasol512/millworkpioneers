from django.contrib import admin

from .models import Company, Client, Quote

class CompanyAdmin(admin.ModelAdmin):
    pass

class ClientAdmin(admin.ModelAdmin):
    ''' Custom Client  admin '''
    list_display = [
        "name",
        "website",
        "headline",
    ]
    list_display_links = [
        "name",
        "website",
        "headline",
    ]

class QuoteAdmin(admin.ModelAdmin):
    ''' Custom Quote admin '''
    list_display =[
        'id',
        'name',
        'phone',
        'email',
        'company',
        'project',
        'start_date',
        'created_at'
    ]
    list_display_links = [
        'id',
        'name',
        'phone',
        'email',
        'company',
        'project',
        'start_date',
        'created_at'

    ]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Quote, QuoteAdmin)
