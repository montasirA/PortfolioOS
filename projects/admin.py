
from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "featured",
        "display_order",
    )

    list_editable = (
        "featured",
        "display_order",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    search_fields = (
        "title",
    )