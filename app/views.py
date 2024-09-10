# Create your views here.

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import UserForm, ProfileForm


def user_registration(request: HttpRequest) -> HttpResponse:
    user_form = UserForm(label_suffix="")
    profile_form = ProfileForm(label_suffix="")
    context = {'user_form': user_form, 'profile_form': profile_form}

    if request.method == 'POST' and request.FILES:
        user_form_data = UserForm(request.POST)
        profile_form_data = ProfileForm(request.POST, request.FILES)

        if user_form_data.is_valid() & profile_form_data.is_valid():
            new_user = save_user_with_encrypted_password(user_form_data)
            save_profile_with_user(profile_form_data, new_user)
            return HttpResponse('<script>alert("Sign Up Successful")</script>')
        else:
            return HttpResponse('<script>alert("Invalid Data")</script>')
    return render(request, 'User_Registration.html', context)


def save_user_with_encrypted_password(user_form_data):
    new_user = user_form_data.save(commit=False)
    saved_password = user_form_data.cleaned_data["password"]
    new_user.set_password(saved_password)
    new_user.save()
    return new_user


def save_profile_with_user(profile_form_data, user):
    new_profile = profile_form_data.save(commit=False)
    new_profile.username = user
    new_profile.save()
