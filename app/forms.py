from django import forms

from app.models import User, Profile

LABEL_SUFFIX_DASH = '-'
LABEL_SUFFIX_SPACE = ' '


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput}
        help_texts = {'username': ''}
        label_suffix = LABEL_SUFFIX_DASH


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'profile_pic']
        label_suffix = LABEL_SUFFIX_SPACE
