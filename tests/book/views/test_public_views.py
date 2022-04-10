from django.test import TestCase
from django.test.client import Client
from star_ratings.models import Rating

from bookaccino.book.models import Book, Genre, Quote

MODELS = [Rating, Genre, Book, Quote]


def createObjects():
    Genre.objects.create(name='Test')
    Quote.objects.create(text='Random quote')

    for x in range(3):
        Book.objects.create(
            title=f'book {x}',
            genre_id=Genre.objects.first().id,
            image='fake-img.jpg'
        )


class PublicViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        createObjects()

    def tearDown(self):
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_getProfilesIndex_shouldRenderTemplate(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'profiles/home-no-profile.html')
