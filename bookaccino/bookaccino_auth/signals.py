from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from bookaccino import settings
from bookaccino.bookaccino_auth.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(user_created, sender=settings.AUTH_USER_MODEL)
