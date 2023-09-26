from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'surname', 'name', 'password1', 'password2', 'phone', 'avatar', 'city')


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'surname', 'name', 'phone', 'avatar', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class PasswordResetForm(forms.Form):
    email = forms.EmailField()