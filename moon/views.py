from django.shortcuts import render
from .forms import IdolForm, IdolTitleForm
from django.shortcuts import redirect
from .models import IdolImage


def upload(request):
    if request.method == 'POST':
        form = IdolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('idol-home')
    else:
        form = IdolForm()
    return render(request, 'idol/upload.html', {'form': form})

def idol_home(request):
    idols = IdolImage.objects.order_by('title').all()
    return render(request, 'idol/idol-home.html', {'idols': idols})

def detail(request, pk):
    idol = IdolImage.objects.get(pk=pk)
    if request.method == 'POST':
        form = IdolTitleForm(request.POST)
        if form.is_valid():
            idol.title = form.cleaned_data['title']
            idol.save()
            return redirect('idol-detail', pk=idol.pk) # 수정 후 상세 페이지로 다시 리디렉션
    form = IdolTitleForm(initial={'title': idol.title})
    return render(request, 'idol/detail.html', {'idol': idol, 'form': form})

def delete(request, pk):
    if request.method == 'POST':
        image = IdolImage.objects.get(pk=pk)
        image.delete()
        return redirect('idol-home')
    image = IdolImage.objects.get(pk=pk)
    return render(request, 'idol/delete.html', {'image': image})

def idol_edit(request, pk):
    if request.method == 'POST':
        form = request.form.get('title')
        if form.is_valid():
            idol = IdolImage.objects.get(pk=pk)
            idol.title = form.cleaned_data['title']
            form.save()
            return redirect('idol-home')
    return render(request, 'idol/upload.html', {'form': form})