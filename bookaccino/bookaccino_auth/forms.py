from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):  # Add back args and kwargs
        super(SignUpForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UserModel
        fields = ("email",)


class SignInForm(AuthenticationForm):
    user = None

    def __init__(self, *args, **kwargs):  # Add back args and kwargs
        super(SignInForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        super().clean()
        self.user = authenticate(
            email=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Email and/or password incorrect')

    def save(self):
        return self.user

