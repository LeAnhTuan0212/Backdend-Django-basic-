from django.shortcuts import render
from django.http import HttpResponse

from .forms import PostForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def add_post(request):
    a = PostForm()
    return render(request, 'news/add_news.html', {'f':a})

def save_news(request):
    if request.method == "POST":
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("Saved...")
        else:
            return HttpResponse("It is not validate.")
    else:
        return HttpResponse("This request is not POST.")
