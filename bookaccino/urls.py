
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookaccino.book.urls')),
    path('auth/', include('bookaccino.bookaccino_auth.urls')),
    path('profile/', include('bookaccino.profiles.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
