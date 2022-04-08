from django import forms
from .models import Comment
from bookaccino.book import models
from bookaccino.book.models import Book, ProfileBook


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class ProfileBookStateForm(forms.ModelForm):
    class Meta:
        model = ProfileBook
        fields = ('book_state',)
        labels = {
            'book_state': '',
        }


class AddBookForm(BookForm):
    genres = forms.ModelChoiceField(models.Genre.objects.all())
    pass


class DetailsBookForm(BookForm):
    pass


class EditBookForm(BookForm):
    pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            "text": "What did you think?"
        }
