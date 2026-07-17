from django.shortcuts import render, redirect

from .models import (
    About,
    Hero,
    Skill,
    ContactInfo,
    ContactMessage,
    Now
)

from projects.models import Project
from blog.models import Blog

from .forms import ContactForm



def home(request):

    hero = Hero.objects.first()

    about = About.objects.first()

    skills = Skill.objects.filter(
        is_active=True
    ).order_by(
        "display_order"
    )

    featured_projects = Project.objects.filter(
        featured=True
    ).order_by(
        "display_order"
    )

    contact = ContactInfo.objects.first()

    now = Now.objects.first()


    featured_blogs = Blog.objects.filter(
        published=True
    ).order_by(
        "-created_at"
    )[:3]



    # Contact Form Handling

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("home")


    else:

        form = ContactForm()



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


    return render(
        request,
        "home/index.html",
        context
    )



def contact_view(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("home")


    else:

        form = ContactForm()


    return render(
        request,
        "home/contact.html",
        {
            "form": form
        }
    )