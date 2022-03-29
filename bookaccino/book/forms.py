from django import forms

from bookaccino.book.models import Book, Image, Comment, ProfileBook


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class ProfileBookStateForm(forms.ModelForm):
    class Meta:
        model = ProfileBook
        fields = ('book_state',)


class AddBookForm(BookForm):
    pass


class DetailsBookForm(BookForm):
    pass


class EditBookForm(BookForm):
    pass


