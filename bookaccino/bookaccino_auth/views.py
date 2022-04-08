from django.contrib.auth import logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from bookaccino.bookaccino_auth.forms import SignInForm, SignUpForm

UserModel = get_user_model()


class SignInView(LoginView):
    template_name = 'auth/sign-in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('home')


class SignUpView(CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse('home')

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['request'] = self.request
        return form_kwargs


@login_required
def sign_out(request):
    logout(request)
    return redirect('home')


