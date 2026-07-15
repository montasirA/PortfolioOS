from django.contrib import admin
from .models import (
    About,
    Hero,
    Skill,
    ContactInfo,
    ContactMessage,
    Now,
)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "projects_completed",
        "years_of_experience",
        "happy_clients",
    )


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "headline",
        "available_for_work",
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "percentage",
        "display_order",
        "is_active",
    )

    list_editable = (
        "percentage",
        "display_order",
        "is_active",
    )

#contact form er jnno
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):

    list_display = (
        "email",
        "phone",
        "location",
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
        "is_read",
    )

    list_editable = (
        "is_read",
    )

    readonly_fields = (
        "created_at",
    )

@admin.register(Now)
class NowAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "learning",
        "status",
        "updated_at",
    )