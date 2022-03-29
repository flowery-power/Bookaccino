from django.urls import path

from bookaccino.book import views
from bookaccino.book.views import BookCreateView, BookEditView, book_details, BookDeleteView, genres, \
    LikeBookView, LoggedInHome, PublicHome
from bookaccino.core.utils import logged_in_switch_view

urlpatterns = [
    path('', logged_in_switch_view(
        LoggedInHome.as_view(), PublicHome.as_view()
    ), name='home'),
    path('add/', BookCreateView.as_view(), name='create book'),
    path('edit/<int:pk>', BookEditView.as_view(), name='edit book'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='delete book'),
    path('details/<int:pk>', views.book_details, name='details book'),
    # path('details/<int:pk>', BookDetailsView.as_view(), name='details book'),
    path('like/<int:pk>', LikeBookView.as_view(), name='like book'),
    path('genres/<int:pk>', genres, name='genres'),
    path('search/', views.search, name='search'),
    path('books/', views.books, name='books'),

]
