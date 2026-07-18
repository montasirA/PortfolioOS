from django.contrib import admin
from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ("image", "caption", "display_order")


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

    inlines = (
        ProjectImageInline,
    )