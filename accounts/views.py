from django.shortcuts import render, redirect
from .forms import EmailUserCreationForm, EmailAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def register_view(request):
    form = EmailUserCreationForm()
    if request.method == 'POST':
        form=EmailUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    form = EmailAuthenticationForm(request)
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
        else:
            print(form.errors)  # Reveals the exact validation failure
    return render(request, 'account/login.html', {'form': form})


