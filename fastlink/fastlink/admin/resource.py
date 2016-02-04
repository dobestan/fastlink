from django.contrib import admin

from fastlink.models import Resource


@admin.register(Resource)
class ResourceModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'course',

        'url',
        'description',
    )

    list_filter = admin.ModelAdmin.list_filter + (
        'course',
    )

    inlines = (
    )

    search_fields = (
        'course',

        'url',
        'description',
    )

    readonly_fields = (
    )
