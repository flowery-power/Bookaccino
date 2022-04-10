from django.test import TestCase
from django.test.client import Client
from star_ratings.models import Rating

from bookaccino.book.models import Book, Genre, Quote
from bookaccino.bookaccino_auth.models import BookaccinoUser, Profile
from tests.create_objects import createObjects


class ProfileViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = BookaccinoUser.objects.create_user('blah@blah.com', 'testpassword')
        self.test_user.is_superuser = True
        self.test_user.is_active = True
        self.test_user.profile = Profile()
        self.test_user.save()
        self.assertEqual(self.test_user.is_superuser, True)
        login = self.client.login(username='blah@blah.com', password='testpassword')
        self.failUnless(login, 'Could not log in')

    def test_signup_view(self):
        response = self.client.get('/auth/sign-up/')
        self.assertTemplateUsed(response, 'auth/sign-up.html')

    def test_signin_view(self):
        response = self.client.get('/auth/sign-in/')
        self.assertTemplateUsed(response, 'auth/sign-in.html')

    def test_signout_view(self):
        createObjects()

        response = self.client.get('/auth/sign-out/')
        self.assertRedirects(response, '/')
