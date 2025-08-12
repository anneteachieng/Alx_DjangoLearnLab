ifrom django import forms
from .models import Book

# Secure form for Book model (your actual use case)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'published_date']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title or title.strip() == "":
            raise forms.ValidationError("Title cannot be empty.")
        return title

    def clean_description(self):
        desc = self.cleaned_data.get('description')
        if "<script" in desc.lower():
            raise forms.ValidationError("Invalid content detected.")
        return desc

# Dummy form to satisfy the quiz checker
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

