from django.contrib import admin
from django.utils.html import format_html

from bookaccino.book.models import Book, Genre, ProfileBook, Quote, Comment
from bookaccino.bookaccino_auth.models import Profile


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')
    list_display = ('id', 'thumbnail', 'title',)
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.image.url))

    thumbnail.short_description = 'Book Image'
    list_display = ('title', 'author', 'genre')
    list_display = ('id', 'thumbnail', 'title',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "genre_id":
            kwargs["queryset"] = Genre.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)




admin.site.register(ProfileBook)
admin.site.register(Genre)
admin.site.register(Quote)
admin.site.register(Comment)



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
