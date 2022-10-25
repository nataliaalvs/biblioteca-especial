from django.utils.translation import gettext_lazy as _
from django import forms
from .models import *
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'path']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control mt-2 mb-3'
                },
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control mt-2 mb-3'
                },
            ),
            'path': forms.FileInput(
                attrs={
                    'class': 'form-control-file mt-2 mb-3'
                },
            ),

        }
        labels = {
            'title': _('Título do livro'),
            'author': _('Autor'),
            'path': _('Arquivo'),
        }