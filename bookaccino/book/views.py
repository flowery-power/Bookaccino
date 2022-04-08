from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
import random

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic import TemplateView, FormView, CreateView

from bookaccino.book.forms import ProfileBookStateForm, CommentForm
from bookaccino.book.models import Book, Genre, Quote, ProfileBook, Comment
from bookaccino.core.BootstrapFormMixin import BootstrapFormViewMixin


class PublicHome(TemplateView):
    template_name = "profiles/home-no-profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        most_rated = Book.objects.filter(ratings__isnull=False).order_by('ratings__average').order_by(
            'ratings__count').reverse()[:3]
        context['books_recommendation'] = most_rated
        random_books = random.sample(list(Book.objects.all()), 3)
        context['listopia'] = random_books
        context['recently'] = Book.objects.all().order_by('created_date')[:3]

        items = list(Quote.objects.all())
        random_items = random.sample(items, 1)
        context['quote'] = random_items[0]

        if most_rated:
            context['mostPopular'] = most_rated[0]
        else:
            context['mostPopular'] = random.sample(list(Book.objects.all()), 1)[0]

        return context


class LoggedInHome(LoginRequiredMixin, TemplateView):
    template_name = "profiles/home-with-profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()[:3]
        context['listopia'] = Book.objects.all()[3:6]
        context['recently'] = Book.objects.all()[6:9]

        user_books = self.request.user.profile.books.all()

        currently_reading = user_books.filter(profilebook__book_state='reading')[0:3]
        read = user_books.filter(profilebook__book_state='read')[0:3]
        want_to_read = user_books.filter(profilebook__book_state='want_to_read')[0:3]

        context['currently_reading'] = currently_reading
        context['read'] = read
        context['want_to_read'] = want_to_read

        return context


class BookCreateView(BootstrapFormViewMixin, views.CreateView):
    model = Book
    template_name = 'books/book-add.html'
    success_url = reverse_lazy('home')
    fields = '__all__'


class BookEditView(BootstrapFormViewMixin, views.UpdateView):
    model = Book
    template_name = 'books/book-edit.html'
    success_url = reverse_lazy('home')
    fields = '__all__'


class BookDetailsView(FormView, views.DetailView):
    model = Book
    template_name = 'books/book-details.html'
    object = None
    form_class = ProfileBookStateForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Book.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = random.sample(list(Book.objects.all()), 3)

        profile_book = ProfileBook.objects.filter(book_id=self.object.id)
        form = self.get_form()
        if profile_book:
            form.fields['book_state'].initial = profile_book[0].book_state
        context['book'] = self.object
        context['form'] = form
        context['books'] = books

        return context

    def post(self, request, *args, **kwargs):
        book = Book.objects.filter(id=kwargs.get('pk'))[0]
        profile_book_set = ProfileBook.objects.filter(book_id=book.id)
        if profile_book_set.count():
            profile_book = profile_book_set.first()
        else:
            profile_book = ProfileBook()
        form = ProfileBookStateForm(request.POST)
        if form.is_valid():
            profile_book.book_state = form.cleaned_data['book_state']
            profile_book.book = book
            profile_book.profile = request.user.profile
            profile_book.save()
        return redirect('details book', pk=book.id)


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'books/comment-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book_id = self.kwargs['pk']
        return super().form_valid(form)


class BookDeleteView(BootstrapFormViewMixin, views.DeleteView):
    model = Book
    template_name = 'books/book-delete.html'
    success_url = reverse_lazy('home')
    fields = '__all__'


def books(request):
    user_books = request.user.profile.books.all()
    currently_reading = user_books.filter(profilebook__book_state='reading')
    want_to_read = user_books.filter(profilebook__book_state='want_to_read')
    read = user_books.filter(profilebook__book_state='read')

    paginator_current = Paginator(currently_reading, 3)
    page = request.GET.get('page')
    page_current = paginator_current.get_page(page)

    paginator_want = Paginator(want_to_read, 3)
    page_want = paginator_want.get_page(page)

    paginator_read = Paginator(read, 3)
    page_read = paginator_read.get_page(page)

    data = {
        'books': books,
        'page_current': page_current,
        'page_want': page_want,
        'page_read': page_read

    }
    return render(request, 'books/books.html', data)


def genres(request, pk):
    genre = Genre.objects.get(pk=pk)
    books_by_genre = genre.book_set.all()
    paginator = Paginator(books_by_genre, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    data = {
        'page_obj': page_obj,
        'genre': genre,
    }
    return render(request, 'books/genres.html', data)
