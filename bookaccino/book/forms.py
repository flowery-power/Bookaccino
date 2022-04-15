from django import forms
from .models import Comment
from bookaccino.book.models import ProfileBook


class ProfileBookStateForm(forms.ModelForm):
    class Meta:
        model = ProfileBook
        fields = ('book_state',)
        labels = {
            'book_state': '',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            "text": "What did you think?"
        }
