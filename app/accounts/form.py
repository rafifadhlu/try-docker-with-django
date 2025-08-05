from django import forms
from .models import UserAva
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm

class UploadAvaForm(forms.ModelForm):
    class Meta:
        model   = UserAva
        fields  = ['ava']
        widgets = {
            'ava': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'ava': 'Upload Ava'
        }


class RegisterUserForm(forms.ModelForm):  # ✅ correct base class
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(),
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
        }
        labels = {
            'username': 'Username',
            'password': 'Password',
            'email': 'Email',
        }