from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'photo']
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'author': 'Autor',
            'photo': 'Foto'
        }