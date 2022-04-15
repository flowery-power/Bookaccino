from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views

from django.urls import reverse_lazy
from django.views.generic import FormView

from bookaccino.bookaccino_auth.models import Profile
from bookaccino.core.BootstrapFormMixin import BootstrapFormViewMixin
from bookaccino.profiles.forms import ProfileForm


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


class ProfileEditView(BootstrapFormViewMixin, views.UpdateView):
    model = Profile
    template_name = 'profiles/profile-edit.html'
    success_url = reverse_lazy('home')
    fields = ('first_name', 'last_name', 'profile_image')

