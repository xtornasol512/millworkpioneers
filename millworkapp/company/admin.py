from django.contrib import admin

from .models import Company, Client

class CompanyAdmin(admin.ModelAdmin):
    pass

class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Company, CompanyAdmin)
admin.site.register(Client, ClientAdmin)
