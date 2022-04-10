from unittest import TestCase

from bookaccino.bookaccino_auth.forms import SignUpForm


class SignUpFormTests(TestCase):
    def test_title_starting_lowercase(self):
        form = SignUpForm(data={"email": "some@email.com", "password": "some-pass123"})

        self.assertEqual(
            form.errors["title"], ["Should start with an uppercase letter"]
        )

    # def test_title_ending_full_stop(self):
    #     form = SignUpForm(data={"email": "some@email.com", "password": "some-pass123"})
    #
    #     self.assertEqual(form.errors["title"], ["Should not end with a full stop"])
    #
    # def test_title_with_ampersand(self):
    #     form = SignUpForm(data={"email": "some@email.com", "password": "some-pass123"})
    #
    #     self.assertEqual(form.errors["title"], ["Use 'and' instead of '&'"])