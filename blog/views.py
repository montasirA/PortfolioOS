from django.shortcuts import render, get_object_or_404

from .models import Blog


def blog_list(request):

    blogs = Blog.objects.filter(
        published=True
    )

    context = {

        "blogs": blogs,

    }

    return render(
        request,
        "blog/blog_list.html",
        context,
    )


def blog_detail(request, slug):

    blog = get_object_or_404(
        Blog,
        slug=slug,
        published=True,
    )

    context = {

        "blog": blog,

    }

    return render(
        request,
        "blog/blog_detail.html",
        context,
    )