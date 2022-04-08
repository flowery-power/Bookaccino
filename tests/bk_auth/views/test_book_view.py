

from django.test import TestCase
from django.test.client import Client

# from app.models import SampleModel

# MODELS = [SampleModel]
from bookaccino.book.models import Book, Genre
from bookaccino.bookaccino_auth.models import BookaccinoUser, Profile


class BookViewTests(TestCase):
    # fixtures = ['test_data', ]

    def createObjects(self):
        Genre.objects.create(name='Test')
        self.book = Book.objects.create(
            title='book',
            genre_id=Genre.objects.first().id,
            image='fake-img.jpg'
        )

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
        # for model in MODELS:
        #     for obj in model.objects.all():
        #         obj.delete()

    def test_samplemodel_list(self):
        """This tests the samplemodel-listview, ensuring that templates are loaded correctly.
        This view uses a user with superuser permissions so does not test the permission levels for this view."""

        test_response = self.client.get('/samplemodel/')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('samplemodel_list' in test_response.context)
        self.assertTemplateUsed(test_response, 'samplemodel_list.html')
        self.assertEqual(test_response.context['samplemodel_list'][1].pk, 1)
        self.assertEqual(test_response.context['samplemodel_list'][1].name, u'Sample Model Instance Name')

    def test_book_details_view(self):
        test_response = self.client.get('/genres/1/')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('book' in test_response.context)
        self.assertTemplateUsed(test_response, 'books/book-details.html')
        self.assertEqual(test_response.context['book'].pk, 1)
        self.assertEqual(test_response.context['book'].name, u'Sample Model Instance Name')

    def test_samplemodel_view_create(self):
        """This tests the samplemodel-new view, ensuring that templates are loaded correctly.
        This view uses a user with superuser permissions so does not test the permission levels for this view."""

        test_response = self.client.get('/samplemodel/new/')
        self.assertEqual(test_response.status_code, 200)
        self.assertTemplateUsed(test_response, 'base.html')
        self.assertTemplateUsed(test_response, 'samplemodel_form.html')

    def test_samplemodel_view_edit(self):
        """This tests the samplemodel-edit view, ensuring that templates are loaded correctly.
        This view uses a user with superuser permissions so does not test the permission levels for this view."""

        test_response = self.client.get('/samplemodel/1/edit/')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('samplemodel' in test_response.context)
        self.assertTemplateUsed(test_response, 'samplemodel_form.html')
        self.assertEqual(test_response.context['samplemodel'].pk, 1)
        self.assertEqual(test_response.context['samplemodel'].name, u'Sample Model Instance Name')

        # verifies that a non-existent object returns a 404 error presuming there is no object with pk=2.
        null_response = self.client.get('/samplemodel/2/edit/')
        self.assertEqual(null_response.status_code, 404)

    def test_samplemodel_view_delete(self):
        """This tests the samplemodel-delete view, ensuring that templates are loaded correctly.
        This view uses a user with superuser permissions so does not test the permission levels for this view."""

        test_response = self.client.get('/samplemodel/1/delete/')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('samplemodel' in test_response.context)
        self.assertTemplateUsed(test_response, 'confirm_delete.html')
        self.assertEqual(test_response.context['samplemodel'].pk, 1)
        self.assertEqual(test_response.context['samplemodel'].name, u'Sample Model Instance Name')

        # verifies that a non-existent object returns a 404 error.
        null_response = self.client.get('/samplemodel/1/delete/')
        self.assertEqual(null_response.status_code, 404)

