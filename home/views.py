from django.shortcuts import render
from .models import About, Hero, Skill, ContactInfo, ContactMessage, Now
from projects.models import Project
from blog.models import Blog   # Blog model import করতে হবে
from .forms import ContactForm   # ContactForm আলাদা forms.py তে থাকবে

def home(request):
    hero = Hero.objects.first()
    about = About.objects.first()
    skills = Skill.objects.filter(is_active=True).order_by("display_order")
    featured_projects = Project.objects.filter(featured=True).order_by("display_order")
    contact = ContactInfo.objects.first()
    form = ContactForm()
    now = Now.objects.first()

    # এখানে blog queryset define করো
    featured_blogs = Blog.objects.filter(published=True).order_by("-created_at")[:3]

    context = {
        "hero": hero,
        "about": about,
        "skills": skills,
        "featured_projects": featured_projects,
        "contact": contact,
        "form": form,
        "featured_blogs": featured_blogs,
        "now": now,
    }
    return render(request, "home/index.html", context)


def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        # success message দেখাতে চাইলে এখানে redirect করতে পারো
    return render(request, "home/contact.html", {"form": form})
