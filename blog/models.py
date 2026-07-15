from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=250)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    cover_image = models.ImageField(
        upload_to="blogs/",
        blank=True,   # optional রাখলে error কম হবে
        null=True
    )

    short_description = models.TextField()

    content = models.TextField()

    category = models.CharField(
        max_length=100,
        default="General"
    )

    reading_time = models.PositiveIntegerField(
        default=5,
        help_text="Estimated reading time in minutes"
    )

    featured = models.BooleanField(default=False)

    published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
