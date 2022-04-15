
from django import forms

from bookaccino.bookaccino_auth.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileForm):
    class Meta:
        fields = ('first_name', 'last_name', 'profile_image')




