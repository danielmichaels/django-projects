from django.shortcuts import render

from blog_content.models import Post


def home(request):
    posts = Post.objects.all()
    context = {"title": "blogZzZ", "posts": posts}
    return render(request, "blog_content/home.html", context)


def about(request):
    context = {}
    return render(request, "blog_content/about.html", context)
