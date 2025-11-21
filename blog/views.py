from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm

def blog_home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def blog_create(request):
    user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "새로운 글이 등록되었습니다.")
            return redirect('blog-home')
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})

def blog_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "글이 수정되었습니다.")
            return redirect('blog-home')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/update.html', {'form': form})

def blog_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        messages.success(request, "글이 삭제되었습니다.")
        post.delete()
        return redirect('blog-home')
    else:
        return render(request, 'blog/delete.html', {'post': post})

def index(request):
    return render(request, 'index.html')