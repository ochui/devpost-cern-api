from django.contrib import admin
from api.models import Resource, ResourceManger


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):

    list_display = [
        'resource_type',
        'resource_status',
        'state', 'lga'
    ]
    list_editable = ['resource_status']


@admin.register(ResourceManger)
class ResourceMangerAdmin(admin.ModelAdmin):

    list_display = ['name', 'resource_type']
