from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# message.debug, info, success, warning, error

def logout_view(request):
    auth.logout(request)
    return redirect('blog-home')
    # return render(request, 'users/logout.html')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')

# Create your views here.