from django.test import TestCase

from bookaccino.book.forms import ProfileBookStateForm


class ProfileBookStateFormTests(TestCase):
    def test_book_state_label(self):
        form = ProfileBookStateForm()

        self.assertEqual(
            form.fields['book_state'].label, ""
        )
