from django.shortcuts import get_object_or_404, render

from .models import Project


def project_detail(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug
    )

    tech_stack = [
        tech.strip()
        for tech in project.tech_stack.split(",")
        if tech.strip()
    ]

    context = {
        "project": project,
        "tech_stack": tech_stack,
    }

    return render(
        request,
        "projects/project_detail.html",
        context,
    )