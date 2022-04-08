from django.contrib.contenttypes.fields import GenericRelation

from django.db import models

from star_ratings.models import Rating

from bookaccino.bookaccino_auth.models import BookaccinoUser, Profile


class Genre(models.Model):
    name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        max_length=80,
    )
    author = models.CharField(
        max_length=50,
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to='books',
    )
    created_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    ratings = GenericRelation(Rating, related_query_name='books')

    def __str__(self):
        return self.title


class ProfileBook(models.Model):
    BOOK_STATE = (
        ('reading', 'Currently Reading'),
        ('read', 'Read'),
        ('want_to_read', 'Want to read'),
        ('not_reading', 'Not reading')
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    book_state = models.CharField(
        max_length=30,
        choices=BOOK_STATE,
        default='not_reading'
    )

    class Meta:
         unique_together= [['profile', 'book']]


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(
        max_length=200,
    )


class Comment(models.Model):
    user = models.ForeignKey(BookaccinoUser, related_name="comments", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    book = models.ForeignKey(Book, related_name="comments", on_delete=models.CASCADE)
