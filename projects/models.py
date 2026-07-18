from django.db import models
from django.utils.text import slugify


class Project(models.Model):

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    cover_image = models.ImageField(
        upload_to="projects/"
    )

    short_description = models.TextField()

    description = models.TextField()

    tech_stack = models.CharField(
        max_length=300,
        help_text="Example: Django, Python, PostgreSQL"
    )

    github_link = models.URLField(blank=True)

    live_demo = models.URLField(blank=True)

    featured = models.BooleanField(default=False)

    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="projects/gallery/"
    )

    caption = models.CharField(
        max_length=255,
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        if self.caption:
            return f"{self.project.title} - {self.caption}"
        return f"{self.project.title} - Image {self.pk}"