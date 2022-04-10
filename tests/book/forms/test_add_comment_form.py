from django.test import TestCase

from bookaccino.book.forms import CommentForm


class CommentFormTests(TestCase):
    def test_text_label(self):
        form = CommentForm(data={"text": "some text"})

        self.assertEqual(
            form.fields['text'].label, "What did you think?"
        )
