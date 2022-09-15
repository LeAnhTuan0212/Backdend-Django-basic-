from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm

# Create your views here.
def index(response):
    return HttpResponse("Hello!")

def add_post(request):
    post = PostForm()
    return render(request, 'news/add_news.html', {'post': post})

def save_news(request):
    if request.method == "POST":
        post = PostForm(request.POST)
        if post.is_valid():
            post.save()
            return HttpResponse("It's saved.")
        else:
            return HttpResponse("It's not valid.")
    else:
        return HttpResponse("It's not POST request.")