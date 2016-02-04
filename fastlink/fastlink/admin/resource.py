from django.contrib import admin
from django.utils.html import format_html


from fastlink.models import Resource


@admin.register(Resource)
class ResourceModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'course',

        'hash_id',

        'url',
        'shorten_url',

        'description',
    )

    list_filter = admin.ModelAdmin.list_filter + (
        'course',
    )

    inlines = (
    )

    search_fields = (
        'course',

        'hash_id',

        'url',
        'description',
    )

    readonly_fields = (
        'hash_id',
        'shorten_url',
    )

    def shorten_url(self, obj):
        return format_html(
            "<a href='{shorten_url}' target='_blank'>{shorten_url}</a>".format(
                shorten_url=obj.get_shorten_url(),
            )
        )
