from django.shortcuts import render
from .forms import ImageForm
from django.shortcuts import redirect
from .models import Image


def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('idol-home')
    else:
        form = ImageForm()
    return render(request, 'idols/upload.html', {'form': form})

def idol_home(request):
    images = Image.objects.order_by('title').all()
    return render(request, 'idols/idol-home.html', {'images': images})

def detail(request, pk):
    image = Image.objects.get(pk=pk)
    return render(request, 'idols/detail.html', {'image': image})

def delete(request, pk):
    if request.method == 'POST':
        image = Image.objects.get(pk=pk)
        image.delete()
        return redirect('idol-home')
    image = Image.objects.get(pk=pk)
    return render(request, 'idols/delete.html', {'image': image})