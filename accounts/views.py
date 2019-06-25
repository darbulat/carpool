from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

from accounts.forms import RegistrationForm, UserEditForm, ProfileEditForm
from accounts.models import Profile


def register(request):

    error = ""
    done = False
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if not form.is_valid():
            error += "Invalid information/ Email already in use."
        else:
            user = form.save(commit=False)
            user.is_active = True
            user.set_password(form.cleaned_data["password1"])
            user.save()
            Profile.objects.create(user=user)
            done = True

    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form, 'error': error, 'done': done, })


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, file=request.FILES,
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(
        request,
        "accounts/edit.html",
        {"user_form": user_form, "profile_form": profile_form},
    )
