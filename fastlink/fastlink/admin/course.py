from django.contrib import admin

from fastlink.models import Course


@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'name',
        'slug',
    )

    list_filter = admin.ModelAdmin.list_filter + (
    )

    inlines = (
    )

    search_fields = (
        'name',
        'slug',
    )

    readonly_fields = (
    )
