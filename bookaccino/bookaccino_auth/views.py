from django.contrib.auth import authenticate, logout, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
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


@login_required
def sign_out(request):
    logout(request)
    return redirect('home')


