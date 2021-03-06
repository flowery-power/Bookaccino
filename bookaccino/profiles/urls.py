from django.urls import path

from bookaccino.profiles.views import ProfileDetailsView, ProfileEditView

urlpatterns = [
    path('details/<int:pk>', ProfileDetailsView.as_view(), name='details profile'),
    path('edit/<int:pk>', ProfileEditView.as_view(), name='edit profile'),
]
