from django import forms
from .models import UserAva

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
