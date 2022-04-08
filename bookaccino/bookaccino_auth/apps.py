from django.apps import AppConfig


class BookaccinoAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookaccino.bookaccino_auth'

    def ready(self):
        # Do not delete!
        import bookaccino.bookaccino_auth.signals
