
from django import forms

from bookaccino.bookaccino_auth.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileForm):
    pass


class EditProfileForm(ProfileForm):
    pass


class DeleteProfileForm(ProfileForm):
    pass





# class SignUpForm(UserCreationForm, BootstrapFormMixin):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.setup_form()
#
#
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('profile_picture',)
