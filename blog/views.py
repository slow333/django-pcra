from django.shortcuts import render
from .models import Post

posts = Post.objects.all()

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def index(request):
    return render(request, 'index.html')