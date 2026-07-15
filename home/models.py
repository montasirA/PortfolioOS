from django.db import models


class About(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    projects_completed = models.PositiveIntegerField(default=0)

    years_of_experience = models.PositiveIntegerField(default=0)

    happy_clients = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "About Section"

#hero model
class Hero(models.Model):

    greeting = models.CharField(
        max_length=100,
        default="👋 Hello, I'm"
    )

    name = models.CharField(
        max_length=100
    )

    headline = models.CharField(
        max_length=200
    )

    description = models.TextField()

    hero_image = models.ImageField(
        upload_to="hero/"
    )

    primary_button_text = models.CharField(
        max_length=50,
        default="View Projects"
    )

    primary_button_link = models.CharField(
        max_length=200,
        default="#projects"
    )

    secondary_button_text = models.CharField(
        max_length=50,
        default="Contact Me"
    )

    secondary_button_link = models.CharField(
        max_length=200,
        default="#contact"
    )

    available_for_work = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name
    
#skill model
class Skill(models.Model):

    name = models.CharField(max_length=100)

    icon = models.ImageField(
        upload_to="skills/"
    )

    color = models.CharField(
        max_length=20,
        default="#FFD54A",
        help_text="Example: #FFD54A"
    )

    percentage = models.PositiveIntegerField(
        default=90
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:

        ordering = ["display_order"]

    def __str__(self):

        return self.name
    
#contact form er jnnno code
class ContactInfo(models.Model):

    email = models.EmailField()

    phone = models.CharField(max_length=30)

    location = models.CharField(max_length=150)

    github = models.URLField(blank=True)

    linkedin = models.URLField(blank=True)

    facebook = models.URLField(blank=True)

    instagram = models.URLField(blank=True)

    whatsapp = models.CharField(
        max_length=30,
        blank=True
    )

    def __str__(self):
        return "Contact Information"


class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Now(models.Model):

    title = models.CharField(
        max_length=100,
        default="Currently"
    )

    project = models.CharField(
        max_length=200
    )

    learning = models.CharField(
        max_length=200
    )

    reading = models.CharField(
        max_length=200,
        blank=True
    )

    drinking = models.CharField(
        max_length=100,
        default="Coffee ☕"
    )

    status = models.CharField(
        max_length=100,
        default="Available for Work"
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return "Now Section"