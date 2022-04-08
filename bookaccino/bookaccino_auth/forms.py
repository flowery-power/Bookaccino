from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    class Meta(UserCreationForm.Meta):
        pass

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            auth_user = authenticate(
                username=self.cleaned_data['email'],
                password=self.cleaned_data['password1']
            )
            login(self.request, auth_user)

        return user

    class Meta:
        model = UserModel
        fields = ("email",)


class SignInForm(AuthenticationForm):
    user = None

    def __init__(self, *args, **kwargs):
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

