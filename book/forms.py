from django import forms
from .models import Book
#Quadri's Ebook Repo
class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'