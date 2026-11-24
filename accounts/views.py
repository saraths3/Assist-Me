from django.shortcuts import render
from .forms import EmailUserCreationForm

def register_view(request):
    form = EmailUserCreationForm()
    if request.method == 'POST':
        form=EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    return render(request, 'account/login.html', {'form': form})