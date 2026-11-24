from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

UserModel = get_user_model()

class EmailUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)

class EmailAuthenticationForm(AuthenticationForm):
        username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"autofocus": True, "placeholder": "you@example.com"}),
    )