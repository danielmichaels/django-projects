from django.shortcuts import render

posts = [
    {'author': 'Roger Ramjet',
     'title': 'blog post 1',
     'content': 'lorem lorem',
     'date_posted': '30 August 2020'},

    {'author': 'Proton Pill',
     'title': 'blog post 2',
     'content': 'lorem lorem',
     'date_posted': '31 August 2020'},
]

def home(request):
    context = {"title": "blogZzZ", 'posts': posts}
    return render(request, "blog_content/home.html", context)


def about(request):
    context = {}
    return render(request, "blog_content/about.html", context)
