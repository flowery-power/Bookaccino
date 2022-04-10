from bookaccino.book.models import Genre, Quote, Book


def createObjects():
    Genre.objects.create(name='Test')
    Quote.objects.create(text='Random quote')

    for x in range(3):
        Book.objects.create(
            title=f'book {x}',
            genre_id=Genre.objects.first().id,
            image='fake-img.jpg'
        )
