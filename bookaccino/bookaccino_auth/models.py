from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import PermissionsMixin


from cloudinary import models as cloudinary_models
from bookaccino.bookaccino_auth.managers import BookaccinoUserManager


class BookaccinoUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = BookaccinoUserManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        blank=True,
        default=""
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
        default=""

    )
    profile_image = cloudinary_models.CloudinaryField(
        resource_type='image',
        blank=True,
    )
    user = models.OneToOneField(
        BookaccinoUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    books = models.ManyToManyField('book.Book', through='book.ProfileBook', blank=True)

    def __str__(self):
        return self.first_name
