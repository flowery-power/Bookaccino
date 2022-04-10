from unittest import TestCase

from bookaccino.bookaccino_auth.forms import SignInForm


class SignInFormTests(TestCase):
    def test_sign_ip_form_username_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your username'
        form = SignInForm()
        self.assertEqual(expected_placeholder, form.fields['username'].widget.attrs['placeholder'])

    def test_sign_in_form_password_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your password'
        form = SignInForm()
        self.assertEqual(expected_placeholder, form.fields['password'].widget.attrs['placeholder'])