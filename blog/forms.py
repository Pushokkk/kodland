from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('published_date',)
        labels = {
            'image': "Файл",
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Введите название'
            })
        }
