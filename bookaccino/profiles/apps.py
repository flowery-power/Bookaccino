from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookaccino.profiles'

    def ready(self):
        import bookaccino.bookaccino_auth.signals