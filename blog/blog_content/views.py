from django.http import HttpResponse

def home(request):
    return HttpResponse('blog-home')

def about(request):
    return HttpResponse("<marquee>helllloooo about</marquee>")
