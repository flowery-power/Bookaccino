import profile

import contex as contex
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin

from bookaccino.book.models import Book
from bookaccino.bookaccino_auth.models import Profile
from bookaccino.core.BootstrapFormMixin import BootstrapFormViewMixin
from bookaccino.profiles.forms import EditProfileForm, ProfileForm



# def profile_details(request):
#     profile = Profile.objects.get(pk=request.user.id)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = ProfileForm(instance=profile)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'profiles/profile-details.html', context)

class ProfileDetailsView(LoginRequiredMixin, FormView):
    model = Profile
    template_name = 'profiles/profile-details.html'
    form_class = ProfileForm
    success_url = reverse_lazy('details profile')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=request.user.id)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile'] = self.object
        return context


# class ProfileEditView(LoginRequiredMixin, BootstrapFormViewMixin,views.UpdateView):
class ProfileEditView(BootstrapFormViewMixin, views.UpdateView):
    model = Profile
    template_name = 'profiles/profile-edit.html'
    success_url = reverse_lazy('home')
    fields = '__all__'


class ProfileDeleteView(LoginRequiredMixin, views.DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('home')
    fields = '__all__'
