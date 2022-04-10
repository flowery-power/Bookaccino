from django.test import TestCase
from django.test.client import Client

from bookaccino.book.models import Book, Genre, Quote
from bookaccino.bookaccino_auth.models import BookaccinoUser, Profile

MODELS = [Genre, Book, Quote]


class BookViewTests(TestCase):

    def createObjects(self):
        self.genre = Genre.objects.create(name='Test')

        for x in range(3):
            book = Book.objects.create(
                title=f'book {x + 1}',
                genre_id=Genre.objects.first().id,
                image='fake-img.jpg'
            )
            self.test_user.profile.books.add(book)

        self.book = Book.objects.create(title=f'book',
                                        genre_id=Genre.objects.first().id,
                                        image='fake-img.jpg')

    def setUp(self):
        """Instantiate the test client.  Creates a test user."""
        self.client = Client()
        self.test_user = BookaccinoUser.objects.create_user('blah@blah.com', 'testpassword')
        self.test_user.is_superuser = True
        self.test_user.is_active = True
        self.test_user.profile = Profile()
        self.test_user.save()
        self.assertEqual(self.test_user.is_superuser, True)
        login = self.client.login(username='blah@blah.com', password='testpassword')
        self.failUnless(login, 'Could not log in')
        self.createObjects()

    def test_getProfilesIndex_shouldRenderTemplate(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'profiles/home-with-profile.html')

    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_profile_books_list(self):
        test_response = self.client.get('/books/')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('page_current' in test_response.context)
        self.assertTrue('page_want' in test_response.context)
        self.assertTrue('page_read' in test_response.context)
        self.assertTemplateUsed(test_response, 'books/books.html')

    def test_book_details_view(self):
        test_response = self.client.get('/details/1')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('book' in test_response.context)
        self.assertTemplateUsed(test_response, 'books/book-details.html')
        self.assertEqual(test_response.context['book'].pk, 1)
        self.assertEqual(test_response.context['book'].title, u'book 1')

    def test_book_view_create(self):
        """This tests the samplemodel-new view, ensuring that templates are loaded correctly.
        This view uses a user with superuser permissions so does not test the permission levels for this view."""

        test_response = self.client.get('/add/')
        self.assertEqual(test_response.status_code, 200)
        self.assertTemplateUsed(test_response, 'books/book-add.html')

    def test_book_view_edit(self):
        """This tests the samplemodel-edit view, ensuring that templates are loaded correctly.
        This view uses a user with superuser permissions so does not test the permission levels for this view."""

        test_response = self.client.get(f'/edit/{self.book.id}')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('book' in test_response.context)
        self.assertTemplateUsed(test_response, 'books/book-edit.html')
        self.assertEqual(test_response.context['book'].pk, self.book.id)
        self.assertEqual(test_response.context['book'].title, u'book')

    def test_book_view_delete(self):
        """This tests the samplemodel-delete view, ensuring that templates are loaded correctly.
        This view uses a user with superuser permissions so does not test the permission levels for this view."""

        test_response = self.client.get(f'/delete/{self.book.id}')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('book' in test_response.context)
        self.assertTemplateUsed(test_response, 'books/book-delete.html')
        self.assertEqual(test_response.context['book'].pk, self.book.id)
        self.assertEqual(test_response.context['book'].title, u'book')

    def test_genres_list(self):
        test_response = self.client.get(f'/genres/{self.genre.id}')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('page_obj' in test_response.context)
        self.assertTrue('genre' in test_response.context)
        self.assertTemplateUsed(test_response, 'books/genres.html')


