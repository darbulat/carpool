from accounts.models import Profile
from carpool.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("birthdate", "avatar")
