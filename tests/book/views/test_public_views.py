from django.test import TestCase
from django.test.client import Client
from star_ratings.models import Rating

from bookaccino.book.models import Book, Genre, Quote
from tests.create_objects import createObjects

MODELS = [Rating, Genre, Book, Quote]


class PublicViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        createObjects()

    def tearDown(self):
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_homeNoProfile_view(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'profiles/home-no-profile.html')
        self.assertTrue('books_recommendation' in response.context)
        self.assertTrue('listopia' in response.context)
        self.assertTrue('recently' in response.context)
        self.assertTrue('most_popular' in response.context)
        self.assertTrue('quote' in response.context)

