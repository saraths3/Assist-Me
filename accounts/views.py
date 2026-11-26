from django.shortcuts import render, redirect
from .forms import EmailUserCreationForm, EmailAuthenticationForm
from django.contrib.auth import login, logout

def register_view(request):
    """
    Registration of User's via Custom UserCreation Form,
    form conatins;
        first_name, last_name, username = email
    """
    form = EmailUserCreationForm()
    if request.method == 'POST':
        form=EmailUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    """
    Authenticate user credentials before login via
    Custom AuthenticationForm.
    """
    form = EmailAuthenticationForm(request)
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
        else:
            print(form.errors)  # Reveals the exact validation failure
    return render(request, 'account/login.html', {'form': form})

def logout_view(request):
    """
    Logout user via logout function.
    """
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'logout_':
            logout(request)
            return redirect('login')
    return render(request, 'account/logout.html')