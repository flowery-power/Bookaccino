from .models import Genre


def genres(request):
    all_genres = Genre.objects.all()
    return {
        'genres': all_genres
    }
