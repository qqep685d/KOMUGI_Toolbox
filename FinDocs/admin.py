from django.contrib import admin
from FinDocs.models import Doc, DocType, Contact, OriginalDocPlace

class DocAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'type', 'content', 'is_public', 'date', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    ordering = ['-id',]
    list_filter = ['type', 'is_public', 'created_at', 'updated_at']
    search_fields = ['title', 'content', 'barcode', 'keywords']

class DocTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'priority', 'remarks']
    list_display_links = ['name']
    ordering = ['priority',]

class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact_to', 'email', 'priority', 'remarks']
    list_display_links = ['contact_to']
    ordering = ['priority',]

class OriginalDocPlaceAdmin(admin.ModelAdmin):
    list_display = ['place', 'priority', 'remarks']
    list_display_links = ['place']
    ordering = ['priority',]

admin.site.register(Doc, DocAdmin)
admin.site.register(DocType, DocTypeAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(OriginalDocPlace, OriginalDocPlaceAdmin)
